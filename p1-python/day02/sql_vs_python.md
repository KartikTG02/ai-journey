# SQL vs Python cheat-sheet

| Oracle SQL | Python | Gotcha |
|---|---|---|
| SUBSTR(s,1,3) | s[0:3] | 0-based, end excluded |
| INSTR(s,'-') | s.find('-') | returns -1 not 0 if missing |
| NVL(x,0) | x if x is not None else 0 | return 0 is x is null |
| TRIM(s) | s.strip() | removes blankspaces around s|
| UPPER(s) / LOWER(s) |s.upper() / s.lower() | converts s to uppercase and lowercase |
| REPLACE(s,'-','_') | s.replace('-','_') | replace '-' with '_' in all the strings|
| LENGTH(s) | len(s) | gives length of string |
| a \|\| b | a + b | concatenates a & b if they are strings|
| s LIKE 'TTB%' | s.startswith("TTB") | returns a boolean values based on when s begins with the string "TTB"|
| s LIKE '%CHIPS%' | "CHIPS" in s | returns a boolean values based on whether s contain the string "CHIPS" |
| TO_CHAR(n,'9,999.99') | f"{n:,.2f}"| adds commas and two decimals points to n |
| TO_NUMBER('12') | int("12") | converts string "12" to integer type |
| LPAD(n,3,'0') | f"{n:03d}" | pads to a total width of 3 |
| IS NULL | is None | whether a variable is null |
| CASE WHEN ... END | x if <condition> else y| if the condition is met, then return x, otherwise y|