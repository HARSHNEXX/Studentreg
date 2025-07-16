
---

## 📘 changelog.md

```markdown
# 🧾 Changelog – Student Admission Register

---
## v0.3 – Modularization and Clean Input Handling (upcoming)

### 🧠 Architecture:
- Program now fully driven by `main()` for top-down control
- Extracted all critical inputs into standalone functions:
  - `get_count(prompt, class_name)`
  - `get_roll(prompt)`
  - `get_reg(prompt)`

### 🔐 Input Validation:
- All numeric inputs checked with:
  - Type safety (`try/except`)
  - Range enforcement (must be positive whole numbers)
- Clean messaging for each error case

### ✨ UX Improvements:
- Dynamic prompts that include class and section name
- Removed cluttered inline validation
- Maintained ASCII UI for consistent branding

### 📌 Ready For v1.0:
- Add multi-student batch entry support
- Add `save_to_csv()` to export admission data
- Add loop with `exit()` support to admit more students without restarting script

## 🚧 Version – v0.2
- Refactor into modular functions:
  - `get_student_count()`
  - `register_students()`



## v0.1 – Initial Release (15 July 2025)

### ✨ Features:
- Terminal-based CLI admission tool
- Accepts section and class details from user
- Accepts number of students with full input validation:
  - Must be numeric
  - Must be a whole number greater than 0
- Assigns:
  - Auto-incrementing Roll Numbers (starts at 1)
  - Auto-incrementing Registration Numbers (starts at 12130)
- Displays registration results with name, roll, reg, class & section

### 💄 UI:
- ASCII-style banner for a professional CLI experience

---


