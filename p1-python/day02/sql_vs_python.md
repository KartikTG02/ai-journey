# SQL vs Python cheat-sheet

| Oracle SQL | Python | Gotcha |
|---|---|---|
| SUBSTR(s,1,3) | s[0:3] | 0-based, end excluded |
| INSTR(s,'-') | s.find('-') | returns -1 not 0 if missing |
| NVL(x,0) | x if x is not None else 0 | |
| TRIM(s) | s.strip() | |
| UPPER(s) / LOWER(s) |s.upper() / s.lower() | |
| REPLACE(s,'-','_') | s.replace('-','_') | |
| LENGTH(s) | len(s) | |
| a \|\| b | a + b | |
| s LIKE 'TTB%' | s.startswith("TTB") | |
| s LIKE '%CHIPS%' | "CHIPS" in s | |
| TO_CHAR(n,'9,999.99') | | |
| TO_NUMBER('12') | int("12") | |
| LPAD(n,3,'0') | f{"n:03d"} | |
| IS NULL | is None | |
| CASE WHEN ... END | x if else y| |