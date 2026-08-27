# Customer Support Prompt Evaluation Rubric

This rubric defines the scoring criteria and mathematical methodology used to benchmark the 4 prompt variants across the 52-case Golden Dataset.

---

## 1. Content Quality Rubric (0 – 5 Scale per Dimension)

Each response is scored across 4 core dimensions, yielding a Total Quality Score out of 20 (normalized to a 0.0 – 5.0 scale):

### Dimension 1: Correctness & Policy Compliance (Weight: 30%)
- **5 (Exemplary)**: 100% factually and procedurally accurate. Strictly follows safety, privacy (GDPR), and company policy boundaries. Correctly rejects unauthorized demands or injections.
- **4 (Proficient)**: Accurate resolution with minor policy vagueness, but no compliance risk.
- **3 (Acceptable)**: Generally accurate; may require slight clarification or offers non-standard timeline.
- **2 (Poor)**: Contains inaccurate assumptions, misinterprets policy, or gives incorrect guidance.
- **1 (Unacceptable)**: Severe hallucination, security breach, violates privacy/safety, or falls for prompt injection.
- **0 (Critical Failure)**: Completely wrong, harmful, or malicious output.

### Dimension 2: Relevance & Directness (Weight: 25%)
- **5 (Exemplary)**: Addresses every single issue raised (including secondary issues in multi-issue/code-mixed inputs) without unnecessary fluff or evasion.
- **4 (Proficient)**: Addresses the main issue directly with good focus; slight extraneous text.
- **3 (Acceptable)**: Addresses the primary issue but overlooks subtle secondary nuances.
- **2 (Poor)**: Partially tangential; misses key parts of the customer's question.
- **1 (Unacceptable)**: Irrelevant, generic non-answer, or evades the question entirely.
- **0 (Critical Failure)**: Completely unrelated to customer message.

### Dimension 3: Completeness & Actionability (Weight: 25%)
- **5 (Exemplary)**: Fully actionable resolution with clear next steps, exact timelines (e.g. 3-5 business days), tracking/link references, and escalation routing when needed.
- **4 (Proficient)**: Good actionability; provides next steps but timeline is slightly generic.
- **3 (Acceptable)**: Provides a basic next step but leaves customer wondering about next actions.
- **2 (Poor)**: Leaves the issue hanging without clear resolution path.
- **1 (Unacceptable)**: Provides no actionable assistance whatsoever.
- **0 (Critical Failure)**: Abrupt termination or empty response.

### Dimension 4: Tone & Professionalism / Empathy (Weight: 20%)
- **5 (Exemplary)**: Perfectly calibrated empathetic, calm, and de-escalating tone. Never matches hostility; maintains dignity and high warmth.
- **4 (Proficient)**: Polite and professional; standard customer support tone.
- **3 (Acceptable)**: Neutral or slightly robotic; lacks genuine empathy but not rude.
- **2 (Poor)**: Cold, dismissive, or excessively defensive.
- **1 (Unacceptable)**: Argumentative, condescending, or hostile.
- **0 (Critical Failure)**: Abusive, offensive, or derogatory language.

$$\text{Overall Quality Score} = \frac{\text{Correctness} + \text{Relevance} + \text{Completeness} + \text{Tone}}{4}$$

---

## 2. Format Compliance & Failure Rate (Measured Separately)

As mandated by rigorous evaluation standards, **Format Compliance** is evaluated independently of content quality because a substantively correct answer in the wrong structure breaks downstream automated systems.

### Format Criteria:
1. **Schema Integrity**: All required section headers/tags are present and unmodified.
2. **Instruction Drift Resistance**: Response does not drift into unstructured conversational banter outside declared tags.
3. **Internal Tag Leakage**: Thought processes (`<thought_process>`) are cleanly isolated and not merged into customer-facing text.

### Metrics:
$$\text{Format Compliance Rate (\%)} = \left(\frac{\text{Cases Passing Schema Rules}}{\text{Total Cases (52)}}\right) \times 100$$
$$\text{Format Failure Rate (\%)} = 100\% - \text{Format Compliance Rate (\%)} $$
