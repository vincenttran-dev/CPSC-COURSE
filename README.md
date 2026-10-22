# Computer Science Coursework

![University of Calgary](https://img.shields.io/badge/University%20of%20Calgary-BSc%20Computer%20Science-C8102E)
![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20progress-2EA44F)

A structured record of my Computer Science coursework at the University of Calgary: study notes, small demonstration programs, and completed assignments.

## Courses

| Course | Title | Term | Status |
| --- | --- | --- | --- |
| [CPSC 231](./CPSC231/) | Introduction to Computer Science for Computer Science Majors I | Fall 2026 | In progress |
| [CPSC 233](./CPSC233/) | Introduction to Computer Science for Computer Science Majors II | TBD | Planned |
| [CPSC 251](./CPSC251/) | Theoretical Foundations of Computer Science I | TBD | Planned |

## Repository Structure

```text
CPSC-COURSE/
├── README.md
├── CPSC231/
│   ├── README.md
│   ├── notes-and-demos/
│   └── assignments/
│       ├── README.md
│       └── assignment-01/
│           ├── README.md
│           ├── bar_chart.py
│           └── specification.pdf
├── CPSC233/
│   ├── notes-and-demos/
│   └── assignments/
└── CPSC251/
    ├── notes-and-demos/
    └── assignments/
```

Every course uses the same two folders:

| Folder | Contents |
| --- | --- |
| `notes-and-demos/` | Concept notes in my own words, short example programs, and ungraded practice |
| `assignments/` | One folder per assignment (`assignment-01/`, `assignment-02/`, …) with the source code and a README |

## Conventions

- **Folders:** lowercase with hyphens, e.g. `assignment-01/`, `notes-and-demos/`
- **Python files:** lowercase with underscores and a `.py` extension, e.g. `bar_chart.py`
- **Notes:** Markdown files named by topic, e.g. `loops-notes.md`
- **Branches:** one branch per piece of work, e.g. `assignment-02`, merged into `main` through a pull request

## Running the Code

Programs target **Python 3**. Several CPSC 231 programs use the course's `SimpleGraphics` library, which is distributed on D2L and is not included here. To run one of them:

1. Place `SimpleGraphics.py` in the same folder as the program.
2. Run it from a terminal in that folder:

   ```bash
   python3 bar_chart.py
   ```

Programs that open a graphics window need to run on a computer with a display, not in a headless environment such as GitHub Codespaces.

## Skills and Tools

- **Language:** Python 3
- **Tools:** Git, GitHub, VS Code, Python IDLE
- **Concepts:** program design, input and output, variables and expressions, control flow, debugging

## Security note for learning demos

Programs in `notes-and-demos/` are coursework experiments, not production-ready applications. In particular, the password-input example under `CPSC231/notes-and-demos/demo loging/` stores an entered password in a plain Python list and uses visible terminal input. **Do not use real passwords with this example** or reuse its approach for storing user credentials. A real authentication system should use a vetted password-hashing library and concealed password entry; never store raw passwords.

## Academic Integrity

Assignment code is published only after its due date, as a record of my own work. If you are currently taking one of these courses, do not copy or submit any code from this repository. Doing so violates the University of Calgary academic integrity policy.

## Author

**Vincent Tran**, BSc Computer Science, University of Calgary
[GitHub](https://github.com/vincenttran-dev)
