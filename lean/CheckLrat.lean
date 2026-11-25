import Std.Tactic.BVDecide.LRAT.Checker
import Std.Tactic.BVDecide.LRAT.Parser

open Std.Sat Std.Tactic.BVDecide

#print axioms LRAT.check_sound

private def words (line : String) : List String :=
  (line.splitOn " ").filter (! ·.isEmpty)

private def parseClause (nvars : Nat) (tokens : List String) :
    Except String (CNF.Clause Nat) := do
  match tokens.reverse with
  | "0" :: rest =>
    rest.reverse.mapM fun token => do
      let some lit := token.toInt? | throw s!"invalid literal {token}"
      if lit == 0 || lit.natAbs > nvars then
        throw s!"literal outside declared range: {lit}"
      return (lit.natAbs - 1, lit > 0)
  | _ => throw "clause must end with a single zero"

private def readCnf (source : String) : Except String (CNF Nat) := do
  let lines := (source.splitOn "\n").map (fun s => s.trimAscii.toString)
  let lines := lines.filter fun s => !s.isEmpty && !s.startsWith "c"
  let first :: rest := lines | throw "CNF missing header"
  let ["p", "cnf", n, m] := words first | throw "invalid DIMACS header"
  let some nvars := n.toNat? | throw "invalid variable count"
  let some nclauses := m.toNat? | throw "invalid clause count"
  if rest.length != nclauses then throw "clause count mismatch"
  return ⟨(← rest.mapM (parseClause nvars ∘ words)).toArray⟩

def main : List String → IO UInt32
  | [cnfPath, lratPath] => do
    let formula ← IO.FS.readFile cnfPath
    let proof ← IO.FS.readBinFile lratPath
    match readCnf formula, LRAT.parseLRATProof proof with
    | .error e, _ | _, .error e =>
      IO.eprintln e
      return 2
    | .ok cnf, .ok actions =>
      if LRAT.check actions cnf then
        IO.println s!"VERIFIED {cnf.clauses.size} clauses, {actions.size} actions"
        return 0
      IO.eprintln "LRAT rejected"
      return 1
  | _ => do
    IO.eprintln "usage: checklrat input.cnf proof.lrat"
    return 2
