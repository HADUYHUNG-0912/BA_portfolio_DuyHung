# Odoo ERP Case Study: CRM & Sales Engineering

> **Assessor Overview & Project Breakdown**  
> **Candidate:** Ha Duy Hung | **Target Role:** Business Analyst (Enterprise ERP / SaaS)  
> **Core Focus:** Lead-to-Order Architecture, Business Rules Specification & C-Level Problem Solving  

---

## 🎯 Executive Summary (Interviewer Perspective)

This directory contains an enterprise-level Business Analysis case study on **Odoo ERP (v19.0)**. Rather than approaching software through standard feature checklists, this project demonstrates end-to-end systems thinking: re-engineering cross-functional workflows, implementing system guardrails (Poka-Yoke), resolving organizational conflicts, and safeguarding cash flow forecasting.

---

## 🚀 What Was Accomplished

### 1. Business Process Re-Engineering & Modeling
* **Lead-to-Order Swimlane (4 Lanes):** Mapped explicit operational boundaries across *Customer*, *Sales Rep*, *Odoo Core*, and *Sales Management*. ([View Diagram](./diagram/CRM_Lead_To_Order_Swimlane_Process.png))
* **Automated Lead Assignment & Anti-Poaching:** Designed a Round-Robin distribution model with a 5-lead/day capacity quota and leave-status synchronization. ([View Diagram](./diagram/CRM_Auto_Assignment_Anti_Poaching_Flow.png))
* **System Scope & Use Case Architecture:** Formulated 18 Use Cases across 4 Actor groups, separating Odoo Standard capabilities from custom Fit-Gap logic. ([View Diagram](./diagram/CRM_System_Use_Case_Overview.png))

### 2. 14 Core Business Rules Framework ([doc/Business_Rules_Analysis.md](./doc/Business_Rules_Analysis.md))
* Detailed specifications across 5 foundational pillars: Data Validation, Computed Values, Approval Gates, 3-Tier Security Matrix, and Automated Escalation Paths.

### 3. C-Level Executive Problem Solving

| Case Study | Problem / Operational Bottleneck | BA Solution & System Mechanism | Business Impact |
| :--- | :--- | :--- | :--- |
| **Case M3: Pipeline & Rotting SLA** ([case.md](./doc/case.md)) | Reps hoarding stale deals, distorting revenue forecasts; closing deals as Lost without valid reasons. | • 14-day Kanban rotting visual cue.<br>• Poka-Yoke constraint enforcing structured lost reason selection. | 100% loss transparency; instant bottleneck detection for CCO. |
| **Case M4: Anti-Poaching & Security** ([case_module_4.md](./doc/case_module_4.md)) | Internal lead fighting in B2C; B2B reps hiding client contact info in personal notebooks out of poaching fears. | • Round-Robin + 5 leads/day quota.<br>• 3-tier access matrix + automated Phone/Email Data Masking. | Eliminated internal friction; zero data leakage upon employee departure. |
| **Case M5: Hybrid Revenue & Slipping Deals** ([case_module_5.md](./doc/case_module_5.md)) | Complex contracts (One-off + MRR); reps sliding deal dates across months to evade KPI penalties. | • Dual-tracking for One-off vs. Recurring Revenue.<br>• Reschedule counter (`count >= 2`) triggering Slipping Deal Flag. | Protected CFO cash flow planning; real-time visibility into net New MRR. |

---

## 💡 Key Business Insights

1. **System Guardrails (Poka-Yoke) Over Administrative Policy:**  
   Managerial reminders fail without software enforcement. Blocking status progression until mandatory structured reasons are captured and activating visual rotting cues eliminate operational debt without managerial micromanagement.

2. **Balancing Operational Transparency with Asset Security:**  
   In multi-team B2B sales, unrestricted access invites internal poaching, while complete data silos create duplicate customer profiles. Implementing **Partial Data Masking** allows reps to verify duplicate accounts while strictly securing contact details and quotes.

3. **Multi-Layered Financial Realism in B2B Contracts:**  
   Treating hybrid contracts as a single lump-sum figure blinds leadership to liquidity risks. Decoupling upfront deployment revenue from Monthly Recurring Revenue (MRR) provides CFOs with reliable cash runway visibility while giving CCOs clean subscriber growth metrics.

---

## 📁 Repository Directory Structure

```
odoo/
├── README.md                                          # Executive summary & assessment overview
├── diagram/                                           # High-resolution visual process models (PNG)
│   ├── CRM_Lead_To_Order_Swimlane_Process.png         # [PNG] Cross-functional 4-swimlane workflow
│   ├── CRM_Auto_Assignment_Anti_Poaching_Flow.png      # [PNG] Round-Robin & anti-poaching decision tree
│   └── CRM_System_Use_Case_Overview.png               # [PNG] CRM functional capability matrix
└── doc/                                               # Business specifications & case studies
    ├── Business_Rules_Analysis.md                     # 14 enterprise business rules catalog
    ├── case.md                                        # M3: Pipeline & Rotting SLA case study
    ├── case_module_4.md                               # M4: Assignment & Anti-poaching case study
    ├── case_module_5.md                               # M5: Hybrid revenue & Slipping deals case study
    ├── CRM_Architecture_ASCII.md                      # Functional capability hierarchy
    ├── CRM_Pain_Points.md                             # Unresolved ERP gaps & fit-gap matrix
    ├── BA_Master_Learning_Plan.md                     # 3-phase BA competency roadmap
    ├── CRM_Learning_Progress.md                       # Evaluation logs & scoring rubrics
    └── Learning_Checklist.md                          # Practical skill verification checklist
```

---

> ⬅️ **Back to Master Portfolio:** [Portfolio Homepage (Root README)](../README.md)
