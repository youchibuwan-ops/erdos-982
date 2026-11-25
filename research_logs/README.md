# Research source inventory

[sources.json](sources.json) records top-level source files and recursively enumerated archive members by raw SHA-256 and length. An exclamation mark followed by a slash marks an archive boundary. [duplicate-files.json](duplicate-files.json) groups identical bytes across sources, including the duplicated 27-file legacy archive. Source labels identify the workspace materials, Gemini proof and certificate material, original proof-pack files, and a linked progress attachment. Paths are relative to the relevant source root.

本地原件保留原样。旧证明、原始中文笔记、旧核验报告和阶段快照通过相对文件名及 SHA-256 定位。原始压缩包未被修补稿覆盖。公开版本只收录经授权的材料。

The archive manifest includes supplied executables for identity tracking. This audit compiled the relevant checker sources and never relied on the bundled binary as a proof. Raw attachments and archives stay outside the Git index because some contain private links or materials whose redistribution terms have yet to be confirmed. A source becomes current only after its exact result, replacements, proof version, and status have been registered.
