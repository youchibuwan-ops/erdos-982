# Certificate catalogue

[Replay ledger](replay.json) records the regenerated CNF, the CNF actually checked, the decompressed RUP digest, the RUP step count, and the completed methods for each branch. [Source inventory](../research_logs/sources.json) contains the archive-member SHA-256 values.

The canonical suite has 124 branch traces: 26 from the 3-to-19 archive, 71 in the 20/21 part of Round 3, 26 in the separate \((8,8,4)\) archive, and one for \(22:(8,8,6)\). Two older alternative traces for \(20:(9,9,2)\) and \(20:(9,8,3)\) are retained for history and add zero profile coverage. The first alternative uses the same formula as Round 3 with a different trace; the second uses a weaker, differently hashed formula. All 27 files in the first legacy ZIP duplicate the early subtree of the 3-to-19 ZIP.

The canonical suite has 6,159,713 RUP additions. The two alternate traces take the historical total to 126 distinct refutations and 6,466,271 additions across 125 distinct full CNFs. Step totals count supplied additions, not trimmed LRAT inference counts.

The original archives and certificate bytes are retained locally. See [reproducibility](../REPRODUCIBILITY.md) for access and verification.
