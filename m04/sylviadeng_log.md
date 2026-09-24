## My Lab Notebook for CS1066 PSet #2

Sylvia Deng

[Video Link](https://drive.google.com/file/d/1kW9NpHIoe7aV6TYz9wIqxPLGRhWobD7l/view?usp=sharing)

----
----

### Describe Your Decomposition Approach

For this task, we can decompose it into four parts. The AI should first work on prompting the user for a company's CIK number. Next, it should retrieve the company's financial data using the SEC EDGAR API with the provided CIK number. 

After we extracted the raw data, we move on to extract and process the company's revenue, net income, and assets over the past 10 years. Finally, create a webpage displaying plots of the extracted data. I chose this approach because each stage does separate work and can be tested separated with distinct outputs. 

----
----

### Document Your Iterations with AI

----

Text of my first prompt:

> In the `m04` directory, build a financial analysis tool using data from the SEC EDGAR API. The final tool should prompt the user for a company's CIK number and generate a webpage containing plots of that company's revenue, net income, and total assets over the past 10 years, or as many years as are available.

> Approach the problem using the following decomposition:

> 1. Prompt the user for a company's CIK number. CIK must contain exactly 10 digits and leading zeros are important.
> 2. Use the CIK to retrieve the company's financial data from the SEC EDGAR API. Set the request header `User-Agent` to `"UniversityStudent your.email@harvard.edu"`.
> 3. From the SEC data, identify and extract annual values for Revenue, Net income, and Total assets. Make sure the years and values are in the correct order.
> 4. Generate a webpage for a simple financial dashboard that vertically stacks three plots (one for revenue, one for net income, and one for total assets). Make sure the plots clearly show the year and are easy to read. Include the company's name and CIK on the page if that information is available. When saving the generated, include the company's name and CIK in the filename.

> All of these pieces should be connected into one tool so that I can run a Python program, enter a CIK, and receive the finished webpage. Also include basic error handling for situations such as an invalid CIK or a failed SEC request.

Reflections on success/failure of this prompt:

*   This prompt worked out pretty well. The resulting webpage displayed all three required plots and they were very easy to read. The webpage itself also had a simple and clear design. 
*   The process of decomposing the task allowed me to think through the task more clearly and fill in details that could've been overlooked.

----

**FINAL REFLECTION:** Review your prompting work. How does your work on this pset compare with that of the first pset?

Compared with my work in the first pset, I think this time I gave AI a clearer description of what I want as the final result. I did not include the task decomposition in the first pset because the tasks were much simpler. For this pset, the task was more complicated and can be naturally divided into several stages, so including my decomposition in the prompt was helpful.  I also included error handling in my prompt in this pset to avoid unnecessary iterations.

----
----

### Handling the Problem's Whitespace

When you have a working solution, write a brief statement describing how you ultimately approached the problem's whitespace. What you might have done differently in hindsight, and why? Or defend why your work was a good approach.

How I approached the problem's whitespace: I decided the overall structure of the tool by decomposing the problem, which helped structure the problem solving process. I also specified what information should be included in the dashboard and how they should be organized in the webpage. I left details like webpage styling, plotting, and implementation details to AI.

I liked this approach because the result was clear and functional, and I did not have to go through many iterations to clarify my requirements. In hindsight, I would probably specify a few more details about how the financial values should be formatted and how missing data should be handled, because this way the results can be more predictable and less prone to unexpected data/behavior.

----
----

### Other's Review

... YOU DO NOTHING HERE; ANOTHER STUDENT WILL COMPLETE THIS PART IN SECTION ...

----
----

### AI's Review

... PASTE AI'S FEEDBACK ON THIS LAB NOTEBOOK HERE ...
