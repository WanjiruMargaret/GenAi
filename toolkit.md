<!--
 Toolkit: Safe Prompt Template

## Purpose

This template provides a guideline for creating safe and structured prompts for AI. It clarifies allowed inputs, forbidden inputs, and provides structures for both code-related and sensitive documentation tasks.

---

## 1. Inputs That Are Allowed

* **Educational queries**

  * Example: "Explain the concept of inheritance in Python."

* **Programming and technical tasks**

  * Example: "Write a JavaScript function to reverse a string."

* **Creative content generation**

  * Example: "Compose a short poem about space exploration."

* **General advice (non-sensitive)**

  * Example: "Provide tips for staying productive while studying."

* **Code or document structure guidance**

  * Example: "Design a Markdown template for meeting notes."

* **Safe simulations or test data**

  * Example: "Generate dummy credit card numbers for testing a payment system."

---

## 2. Inputs That Are Forbidden

* **Illegal instructions**

  * How to commit crimes
  * How to hack or bypass systems

* **Invasion of privacy / personal data requests**

  * Accessing someone else's accounts or messages
  * Collecting personal identifiers without permission

* **Unsafe financial requests**

  * Generating real credit card numbers or bypassing banking security

* **Medical, legal, or safety-critical guidance without proper supervision**

  * Prescriptions, legal strategies, or medical treatments

* **Content promoting violence, harassment, or hate speech**

---

## 3. Structure for Code-Related Tasks

1. **Specify language or environment**

   * Example: "Write a Python script..."

2. **State the goal clearly**

   * Example: "...to find prime numbers up to a given n."

3. **Define input/output expectations**

   * Example: "Input: integer n; Output: list of prime numbers up to n."

4. **Optional constraints or best practices**

   * Example: "Optimize for O(n log log n) time using the Sieve of Eratosthenes."

5. **Optional example for clarity**

   * Example: `Input: 10 → Output: [2, 3, 5, 7]`

**Template Example:**

```text
Language: Python
Goal: Generate a list of prime numbers up to n
Input: Integer n
Output: List of prime numbers
Constraints: Use efficient algorithm, minimize memory usage
Example: Input=10 → Output=[2,3,5,7]
```

---

## 4. Structure for Sensitive Documentation Tasks

1. **Specify document type**

   * Example: "Internal IT Security Guide in Markdown."

2. **Define safe content boundaries**

   * Do not include passwords, personal info, or confidential client data.

3. **Include formatting requirements**

   * Example: headings, bullet points, tables, code snippets

4. **Clarify audience and purpose**

   * Example: "For internal staff training on password safety and phishing awareness."

**Template Example:**

```text
Document Type: Internal Security Policy
Audience: Employees
Content Boundaries: No real passwords or sensitive client data
Formatting: Markdown headings, bullet lists, tables, code snippets
Purpose: Train staff on security best practices
-->