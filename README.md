# Agentic AI PCB Assistant

An intelligent assistant for **automated PCB design reasoning** using agentic AI principles and large language models (LLMs). This system automates the **pre-design workflow** of PCBs — from requirement analysis to validated component selection and manufacturable BOM generation — without the need to train custom ML models.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Architecture](#architecture)  
- [Agents](#agents)  
- [How It Works](#how-it-works)  
- [Technology Stack](#technology-stack)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Overview

Creating a PCB (Printed Circuit Board) involves multiple engineering challenges:  

- Converting and fitting voltages correctly  
- Selecting components based on electrical and mechanical constraints  
- Ensuring manufacturability and compliance  

The **Agentic AI PCB Assistant** simplifies this process by decomposing PCB design into **modular reasoning agents**, which work autonomously and iteratively validate and optimize decisions.

---

## Features

- **End-to-end PCB pre-design automation**  
- **Requirement extraction** from natural language input  
- **Component reasoning** using a structured component database  
- **Layout suggestions** and design validations  
- **Manufacturable BOM generation**  
- **Iterative optimization** for component selection  

---

## Architecture

The system is **agentic**, meaning it is **autonomous and iterative**, not just reactive. The design workflow is split into multiple agents that collaborate to produce validated PCB designs.

---

## Agents

1. **Requirement Agent**  
   - Converts natural language requirements into structured engineering data using NLP.  

2. **Component Agent**  
   - Searches and compares components from a database.  
   - Checks constraints like voltage, current, footprint, and availability.  

3. **Validation Agent**  
   - Evaluates the feasibility of selected components in the current environment.  
   - Provides feedback for adjustments if requirements cannot be met.  

4. **Optimization Agent**  
   - Re-selects components based on validation feedback.  
   - Iteratively improves BOM and layout suggestions.  

---

## How It Works

1. **User Input**: The user provides a description of PCB requirements (voltage ranges, functions, constraints).  
2. **Requirement Extraction**: The **Requirement Agent** converts this into structured engineering specifications.  
3. **Component Reasoning**: The **Component Agent** searches the component database, evaluates compatibility, and selects candidates.  
4. **Validation**: The **Validation Agent** simulates or evaluates feasibility against environmental and design constraints.  
5. **Optimization Loop**: The **Optimization Agent** iteratively selects alternative components if needed.  
6. **Output**: The system generates a validated BOM, layout suggestions, and explanations of design choices.

---

## Technology Stack

- **LLM API**: Local LLM for requirement parsing and reasoning: Transformer Torch 
- **NLP**: Requirement extraction and structured reasoning  
- **Database**: Component database for comparison and selection  
- **Engineering Tools**: Validation tools for electrical and environmental feasibility  

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/agentic-pcb-assistant.git
cd agentic-pcb-assistant