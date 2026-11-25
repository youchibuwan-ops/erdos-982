import Std

def supportGaps (n cap : Nat) : List (Nat × Nat × Nat) :=
  let values := List.range (cap + 1)
  values.flatMap fun a =>
    values.flatMap fun b =>
      values.filterMap fun c =>
        if 0 < c && c ≤ b && b ≤ a && a + b + c == n then
          some (a, b, c)
        else
          none

theorem support20 :
    supportGaps 20 9 =
      [(7, 7, 6), (8, 6, 6), (8, 7, 5), (8, 8, 4),
       (9, 6, 5), (9, 7, 4), (9, 8, 3), (9, 9, 2)] := by decide

theorem support21Short :
    supportGaps 21 8 = [(7, 7, 7), (8, 7, 6), (8, 8, 5)] := by decide

theorem support22Short :
    supportGaps 22 8 = [(8, 7, 7), (8, 8, 6)] := by decide

#print axioms support20
#print axioms support21Short
#print axioms support22Short
