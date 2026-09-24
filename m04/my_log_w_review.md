## My Lab Notebook for CS1066 PSet #2

Baoyue Xing

https://harvard.zoom.us/rec/share/iPFAZWyjpFDA2tsOuoxNwczvKdzqphpZK_NLjAY93PC3gxT6toxacRSfPY3Gt7W4.uybPPoVljtC8Dc8z?startTime=1790215334000


----
----

### Describe Your Decomposition Approach

... YOUR COUPLE OF PARAGRAPHS HERE ...

I would first focus on the user input and data collection process by making sure the program could accept a company’s 10-digit CIK number and use it to connect to the SEC EDGAR API. After that, I would work on identifying and extracting the three required financial measures: revenue, net income, and assets. Then, I would clean and organize the results so that the program keeps the most recent 10 years of annual data when that much data is available.

After finishing the data-processing part, I would move on to the output and presentation side of the project. I planned to create separate plots for revenue, net income, and assets, and then combine those plots into a single webpage. Once the webpage was working, I would test the tool using AMD’s CIK and then try other companies to make sure the program could work with different inputs.

----
----

### Document Your Iterations with AI

----
#### SUBTASK #1: CIK input + SEC API connection

Text of my first prompt:

> In the directory m04, create a Python program called `financial_webapp.py` that asks the user for a company’s 10-digit CIK number and uses it to retrieve company facts from the SEC EDGAR API. Keep the CIK as a string so leading zeros are preserved. Include the required User-Agent header for the SEC request. For now, only print the company name and confirm that the data were retrieved successfully. Do not create any plots or webpage yet.

Reflections on success/failure of this prompt:

*   The initial prompt successfully created a program that accepted a CIK number and retrieved data from the SEC.
*   I didn't clearly specify the value for the User-Agent header, so I wanted to use the instructor-provided placeholder, "UniversityStudent your.email@harvard.edu".
*   I also noticed that the generated script didn't use the Python requests library for the SEC API call.
I revised the prompt to explicitly require the requests library while keeping the rest of the program’s behavior unchanged.

----

Text of my next prompt:

> In the directory m04, update `financial_webapp.py` while keeping the rest of the program’s behavior unchanged. Use the Python requests library to retrieve the company facts from the SEC EDGAR API. Set the User-Agent header exactly to "UniversityStudent your.email@harvard.edu". Also create a requirements.txt file in the m04 directory and include any external Python packages required by the program, such as requests, so they can be installed easily. The program should still ask the user for a company’s 10-digit CIK number, preserve any leading zeros, and print the company name to confirm that the data were retrieved successfully. Do not create any plots or webpage yet.

Reflections on success/failure of this prompt:

*   The revised prompt was much more organized and specific than my initial prompt because it clearly clarified that the SEC request should use the Python requests library and that the User-Agent should use the instructor-provided placeholder.
*   It also clearly asked the AI to create a requirements.txt file in the m04 directory and include the external packages needed by the program, such as requests.

----
#### SUBTASK #2: Extract Revenue, Net Income, and Assets

Text of my first prompt:

> In the directory m04, update `financial_webapp.py` so that it extracts annual revenue, net income, and assets from the SEC company facts data. Keep the existing CIK input and SEC request code unchanged unless a change is necessary for this task. Print the year and value for each of the three financial measures so I can check that the correct data are being retrieved. Do not create any plots or webpage yet.


Reflections on success/failure of this prompt:

*   The prompt is very clear and successful because it only asked the AI to extract the three required financial measures and to keep the existing CIK input and SEC request behavior unchanged.


----
#### SUBTASK #3: Clean and organize the last 10 years

Text of my first prompt:

> In the directory m04, update `financial_webapp.py` so that each of the three financial measures (revenue, net income, and assets), keep only the most recent 10 years of annual data when at least 10 years are available. If fewer than 10 years are available, keep all available years. Keep the data in chronological order from oldest to newest within the selected period. Keep the existing CIK input, SEC request, and financial data extraction behavior unchanged. Print the updated results so I can verify that the correct 10-year period is being selected. Do not create any plots or webpage yet.


Reflections on success/failure of this prompt:

*   The prompt is very clear and successful because it clearly narrowed the task to selecting the most recent 10 years of data


----
#### SUBTASK #4: Create the three plots

Text of my first prompt:

> In the directory m04, update `financial_webapp.py` to create three separate plots using the cleaned 10-year financial data that are already being produced by the program: revenue over time, net income over time, and assets over time. Keep the existing CIK input, SEC request, financial data extraction, and 10-year filtering behavior unchanged. For each plot, use the year on the x-axis and the financial value in USD on the y-axis, and include a clear title and axis labels. Plot the data in chronological order from 2016 to 2025 for AMD based on the current output. For now, only create and display the three plots so I can verify that they look correct. Do not build the final webpage yet.


Reflections on success/failure of this prompt:

*   The prompt is very clear and successful because it clearly states the requirements of the three plots. For example, it specifies the x-axis, y-axis, titles, labels, and chronological order.


----
#### SUBTASK #5: Build the webpage

Text of my first prompt:

> In the directory m04, update `financial_webapp.py` to turn the existing program into a simple Python web app. Keep the existing CIK input logic, SEC request, financial data extraction, 10-year filtering, and plotting behavior unchanged. The webpage should allow the user to enter a company’s 10-digit CIK number and, after submitting it, display the company name followed by the three plots for revenue, net income, and assets stacked vertically on the same page. Keep the webpage clean, simple, and easy to read, and use the existing financial data and plots rather than recreating the data-processing logic. 


Reflections on success/failure of this prompt:

*   The prompt is successful since I clearly tell AI the webpage requirements including the CIK input, company name, and the three financial plots stacked vertically on one page.

*   One thing I didn‘t think about when writing the prompt was which web framework to use. The AI chose Streamlit automatically, which was helpful because it let me turn the existing Python script into a web app without creating a separate frontend or using JavaScript.


----
#### SUBTASK #6: Handle errors

Text of my first prompt:

> In the directory m04, update `financial_webapp.py` so that the Streamlit web app handles common errors without crashing. Add error handling for invalid CIK input, failed SEC API requests, and cases where revenue, net income, or assets data are missing. Show a clear and helpful message on the webpage when an error occurs instead of displaying a traceback. Do not add any new features beyond error handling. 


Reflections on success/failure of this prompt:

*   I think the prompt is successful because I clearly identified several error cases that might happen. However, there could still be other error cases that I didn't specifically mention in the prompt, so the error handling may not cover every possible situation.

----
----

**FINAL REFLECTION:** Review your prompting work. How does your work on this pset compare with that of the first pset?

... YOUR FINAL REFLECTIONS HERE ...

Compared with the first pset, I think my prompts became more organized and specific. I divided the larger problem into six smaller subtasks and clearly stated the instructions of each subtask and which existing behaviors should remain unchanged in each prompt. However, I still needed to clarify some details, such as explicitly requiring the requests library. In the future, I will try to identify these technical requirements more clearly in my initial prompts.


----
----

### Handling the Problem's Whitespace

When you have a working solution, write a brief statement describing how you ultimately approached the problem's whitespace. What you might have done differently in hindsight, and why? Or defend why your work was a good approach.

... YOUR FINAL REFLECTIONS HERE ...

I divided the task into six subtasks and decided the required financial measures, the 10-year period, the basic plot layout, and the error cases that the program should handle. I left the coding details and the choice of web framework to the AI. For example, I didn't specify Streamlit in my prompt, but the AI chose it to build the webpage. I was happy with the final result because it met the main requirements I had set.

In hindsight, I might leave a little more of the visualization design open to the AI next time. For this project, I specified a fairly simple layout for the three plots, but allowing the AI to suggest different plot designs might give me some creative visualization ideas that I didn't considered myself.


----
----

### Other's Review

I think this is a very strong notebook because it shows a clear and thoughtful process for working with AI. You break the project into smaller tasks, which makes the work more manageable and easier to debug. I especially like that you keep the previous behavior unchanged while adding new features, because that shows good software development habits and helps reduce mistakes. Your reflections also make the process easy to follow, and it is clear that you learned from the first pset by making your prompts more specific and more structured.



----
----

### AI's Review

The strongest part of your notebook is the structure of your prompting. You explain the goal, the scope of the task, and the constraints for each stage of the project. This helps the AI produce more focused results and reduces accidental errors. Your prompts also demonstrate improvement from the first pset, because they are more specific and more organized. This suggests that you are learning how to communicate requirements more effectively to AI tools.

There are still a few ways to improve the workflow. In some prompts, you could make the acceptance criteria even more explicit by adding a short checklist of requirements and edge cases. For example, you could include items such as invalid CIK input, missing financial data, fewer than 10 years of records, and failed SEC API requests. You could also ask the AI to explain its assumptions before coding or to propose a validation plan after implementation. These additions would make your prompts even more precise and reduce the chance of missing edge cases.

Overall, this notebook is well organized, reflective, and clearly shows improvement over your earlier work. It demonstrates that you are using AI intentionally and thoughtfully, not just as a shortcut. Your process is strong, and with a bit more explicit specification and validation, it could become even more reliable and professional.



## What stands out in your work

What I find most noteworthy is that your process is already closer to “software specification and iteration” than “just asking AI to code.” You do several things well:

- You break a large task into smaller subproblems.
  - That is excellent practice. It makes the work easier to debug and easier for the AI to complete correctly.
- You preserve prior behavior while adding new features.
  - This is especially strong. In your prompts, you repeatedly say “keep the existing behavior unchanged unless necessary,” which reduces accidental regressions.
- You treat prompt writing as a form of requirements engineering.
  - You specify input format, data source, output, and constraints. That is a mature way to work with AI.
- You reflect on what worked and what failed.
  - This is one of the most valuable parts of your notebook. You noticed when the prompt was incomplete, especially around the User-Agent and the required library. That is exactly the kind of learning students should capture.
- You show real iteration rather than one-shot prompting.
  - You revised the prompt after seeing a gap, which is what good debugging with AI looks like.

The strongest pattern is that you are learning to make the AI do a narrower, more controlled job at each step. That is much better than one giant prompt that tries to solve the whole project at once.

---

## What is especially good about your reflection style

You are not just saying “the AI made it work.” You are asking:

- What exactly did I ask for?
- What was missing?
- What was the result?
- What should I improve next time?

That is the right mindset. It makes your work useful as a learning artifact, not just as a project submission.

---

## Suggestions for improvement next time

Here are the main improvements I would suggest:

### 1) Make the acceptance criteria explicit
In your best prompts, the requirements are clear. I would go one step further and add a short “done when” checklist at the end of each prompt.

Example:
- Program accepts a valid 10-digit CIK
- Leading zeros are preserved
- SEC request includes correct headers
- Output prints the company name
- Data are cleaned to the most recent 10 years
- No extra features are added

This makes it easier for the AI to self-check its work.

### 2) Ask the AI to state assumptions before coding
A strong next-step prompt is:
- “Before writing code, list the assumptions you are making and any ambiguities.”

This helps catch missing details before the AI starts implementing.

### 3) Include edge cases and failure modes up front
You already did this for errors, but I would expand it earlier. For example:
- what if the CIK is not 10 digits?
- what if the SEC returns no company facts?
- what if a company has fewer than 10 years of data?
- what if the financial statement label is slightly different?

If you specify these cases, the AI is less likely to miss them.

### 4) Ask for a quick verification plan
You might add:
- “Explain how you will validate this works.”
- “Suggest 2–3 test cases.”
- “List the commands or checks I should run to confirm the behavior.”

This mirrors real software workflow and keeps the AI from simply generating code without checking it.

### 5) Ask for alternatives or tradeoffs
For bigger design choices, ask:
- “What are two reasonable ways to implement this, and which one do you recommend?”

This gets the AI to explain tradeoffs instead of just giving one solution.

### 6) Keep prompts more “spec-first, code-second”
A very strong structure is:
1. State the goal
2. State constraints
3. State required output
4. State edge cases
5. State validation
6. Then ask for implementation

This is a clear pattern you can reuse across assignments.

---

## Bottom line

Your work is strong because it shows:
- careful decomposition
- iterative refinement
- explicit constraints
- reflection and learning

The biggest next step is to make each prompt even more like a formal specification, with explicit validation criteria and edge cases. That will make your AI-assisted coding more reliable and more teachable.

If you want, I can also turn your notes into a reusable “best prompt template” for future AI-assisted coding assignments.
