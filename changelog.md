
---

## 📘 changelog.md

```markdown
# 🧾 Changelog – Student Admission Register

---

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

## 🚧 Next Planned Version – v0.2
- Refactor into modular functions:
  - `get_student_count()`
  - `register_students()`
- Add support for saving output to `.csv` or `.json`
- Allow `exit` as input anywhere to safely terminate
