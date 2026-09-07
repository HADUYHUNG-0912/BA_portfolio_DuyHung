# HA DUY HUNG | BUSINESS ANALYST PORTFOLIO

<p align="center">
  <a href="https://linkedin.com/in/haduyhung"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:haduyhung0912@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://github.com/HADUYHUNG-0912"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
  <img src="https://img.shields.io/badge/GPA-3.68%2F4.0-brightgreen?style=for-the-badge" alt="GPA">
  <img src="https://img.shields.io/badge/TOEIC-795%2F990-blue?style=for-the-badge" alt="TOEIC">
</p>

---

## 👨‍💼 About Me

Third-year **Management Information Systems (MIS)** student with hands-on **Business Analyst** experience across a live corporate internship and multiple software projects that shipped working prototypes.

* 📍 **Location:** Ho Chi Minh City, Vietnam  
* 📞 **Phone:** (+84) 797 069 812  
* ✉️ **Email:** [haduyhung0912@gmail.com](mailto:haduyhung0912@gmail.com)  
* 🔗 **LinkedIn:** [linkedin.com/in/haduyhung](https://linkedin.com/in/haduyhung)  
* 🐙 **GitHub:** [github.com/HADUYHUNG-0912](https://github.com/HADUYHUNG-0912)  

### 🎯 Career Objective
Currently a **Business Analyst Intern at Vado Sport**, supporting real-world BA documentation and testing workflows. Led business requirements analysis, ERD & SQL database design, and use case / UX flow documentation on system-design projects delivered as functioning applications by engineering teams. Over the next 3 years, aiming to grow into a solid **Business Analyst** role within software/web product development (**SaaS, E-commerce, Enterprise ERP**), owning requirements-to-delivery processes end to end.

---

## 🎓 Education

### **University of Transport Ho Chi Minh City** *(Expected 2028)*
* **Degree:** Bachelor's Degree in Management Information Systems (MIS)
* **Cumulative GPA:** **3.68 / 4.0**

---

## 🛠️ Core Competencies & Skills Toolkit

| Domain | Key Skills & Capabilities |
| :--- | :--- |
| **Requirements Engineering** | Business Requirements Gathering & Analysis, Elicitation (Questionnaires, Stakeholder Interviews), BRD/FRD/SRS/URD Authoring, Acceptance Criteria (AC), Test Case Design |
| **Process & System Modeling** | Business Process Mapping (BPMN / Cross-Functional Swimlane), Context Diagrams, Flowcharts, Use Case Diagramming & Specifications, UX Flow Mapping |
| **Data & Database Architecture** | Entity-Relationship Diagram (ERD), Normalized Data Modeling (3NF), SQL Database Schema Design (DDL/DML, Foreign Keys, Indexing), Data Analysis |
| **Tools & Platforms** | Draw.io, Figma (Wireframing & Prototyping), JIRA (Sprint Planning, AI Workflow Automation), Git/GitHub, Enterprise ERP (Odoo 19) |
| **Languages & Communication** | **English:** TOEIC **795 / 990** \| **Vietnamese:** Native |

---

## 💼 Work Experience & Projects

### 1. 🏢 Business Analyst Intern — Vado Sport *(2026 – Present)*
* **URD Validation & Consistency:** Reviewed and validated the User Requirement Document (URD) for the *SvAuthentic AI Poster Generator* project (authored primarily by the BA lead), checking business rules and acceptance criteria across **6 core screens** for consistency before dev handoff.
* **Test Case Engineering:** Authored **54 test cases** directly derived from URD acceptance criteria, covering template selection, asset upload validation, and AI poster generation flows, providing the dev team a reliable verification baseline.
* **Stakeholder Elicitation:** Designed a structured requirements questionnaire to collect business needs directly from stakeholders, standardizing input gathering prior to requirement drafting.
* **Cross-Functional Coordination:** Supported communication between BA lead and development team to maintain requirement clarity and eliminate ambiguities throughout the project lifecycle.

---

### 2. 🐎 Business Analyst & Project Lead — Horse Racing Management System *(May 2026)*
* **Team Leadership & Agile Execution:** Led a **7-member team**, managing task backlogs and sprint progress in JIRA.
* **AI & Workflow Automation:** Configured an AI agent to automate JIRA and GitHub workflows via API, streamlining issue tracking and repository management.
* **Requirements Specification (SRS):** Authored the System Requirements Specification (SRS), establishing functional requirements and system constraints.
* **Process Modeling:** Designed flowcharts and context diagrams to map system scope and operational logic.
* **End-to-End Delivery:** Delivered a working prototype, coordinating requirements, tooling, and team execution from concept to deployment.

---

### 3. 🎓 Business Analyst — Course & Student Management System (English Center) *(March 2026)*
* **Workflow & Gap Analysis:** Led BA activities in a **4-person team** building a student enrollment and course-scheduling system; analyzed workflows to define functional specs and address operational bottlenecks.
* **Data Modeling:** Designed a comprehensive **20+ entity ERD** in Draw.io for a normalized, scalable relational database.
* **Database Implementation:** Built the SQL schema, defining tables, constraints, primary/foreign keys, and data relationships.
* **Dev Alignment & Delivery:** Handed off requirement specs and data models to the engineering team; successfully shipped as a functioning prototype.

---

## 🌟 Featured Enterprise Case Study: Odoo ERP CRM & Sales Engineering

> 📌 **Direct Link to Project Artifacts:** [Explore the Odoo Case Study Directory (./odoo/)](./odoo/)

A deep-dive enterprise analysis project on **Odoo ERP (v19.0)** focusing on the **Lead-to-Order** lifecycle, business rules specification, and executive problem solving.

```
odoo/
├── README.md                      # Executive summary & Interviewer assessment
├── diagram/                       # High-resolution process diagrams (PNG)
│   ├── CRM_Lead_To_Order_Swimlane_Process.png
│   ├── CRM_Auto_Assignment_Anti_Poaching_Flow.png
│   └── CRM_System_Use_Case_Overview.png
└── doc/                           # Comprehensive business analysis documents
    ├── Business_Rules_Analysis.md # 14 core business rules specifications
    ├── case.md                    # Case M3: Pipeline optimization & 14-day rotting SLA
    ├── case_module_4.md           # Case M4: Round-Robin auto-assignment & Anti-poaching
    └── case_module_5.md           # Case M5: Hybrid revenue (One-off + MRR) & Slipping deals
```

### Key Business Problems Solved in this Case Study:
1. **Preventing Stagnant Deals (Anti-Rotting SLA):** Formulated a 14-day visual rotting indicator on Kanban and built a Poka-Yoke constraint enforcing structured lost reasons for sales loss analysis.
2. **Fair Distribution & Anti-Poaching:** Designed a Round-Robin auto-assignment algorithm with a 5 leads/day capacity quota and solved internal poaching through data masking and a 3-tier role security matrix.
3. **Hybrid Revenue Forecasting:** Architected dual tracking for One-off implementation fees vs. Monthly Recurring Revenue (MRR) and introduced automated Slipping Deal flags (`reschedule_count >= 2`) to protect cash flow forecasting.

👉 **[Read the complete Odoo Case Study & Review Sơ đồ Nghiệp vụ](./odoo/)**

---

## 📜 Certifications

* 🏅 **IT Business Analyst** — Udemy Certificate of Completion
* 🏅 **Google Data Analytics Professional Certificate** — Coursera

---

<p align="center">
  <i>Open to Business Analyst / Associate BA opportunities. Feel free to connect via <a href="mailto:haduyhung0912@gmail.com">Email</a> or <a href="https://linkedin.com/in/haduyhung">LinkedIn</a>!</i>
</p>
