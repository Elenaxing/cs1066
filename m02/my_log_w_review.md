## My Lab Notebook for CS1066 PSet #1

Baoyue Xing

https://harvard.zoom.us/rec/share/veGobLma3SjKkj1ix7BL9ubeCuWPJHZ2Nic84fCkTaVCvffNmuQu9VED1fLBoxf4.TN5sskCbeOKMAMPH

----
----

### SUBTASK #1: Prompt for the Search Term

----
Text of my first prompt:

> Work in the directory `m02`. In the existing script `trends_save.py`, replace the fixed "vide coding" search term with input from the user. Ask for this input when the program starts, allowing either a word or a phrase. Use it to build the Google Trends url, then scrape the data and save it to `scraped_data.csv` as before.

Reflections on success/failure of this prompt:

*   My prompt looks successful for me since AI replaced the fixed "vibe coding" searching term with a request for user input. 
*   I was surprised that the AI also added code to remove extra spaces from the beginning and end of the input and format the search phrase for use in the url, even though I hadn't explicitly requested those details.
*   I ran the updated `trends_save.py` program and also `trends_plot.py` program successfully.

----
**FINAL REFLECTION:** Review your work. Write a brief statement of what you might have done differently in hindsight, or defend why your work was a good approach.

... YOUR FINAL REFLECTIONS HERE ...
I think my approach worked very well because my prompt clearly described the change I wanted, and only one prompt was needed. I reviewed the AI's changes and ran the updated program successfully. In hindsight, I could have been more specific about handling extra spaces and phrases in the search input, although the AI addressed those details without being asked.
----
----

### SUBTASK #2: Just One Tool

----
Text of my first prompt:

> Work in the directory `m02`. Create a new python script called `my_tool.py` that runs `trends_save.py` and then `trends_plot.py`. The user should be able to enter a search term and generate its plot by running only `my_tool.py`. Reuse the existing scripts' functions. Keep `scraped_data.csv` so I can check the data afterward.

Reflections on success/failure of this prompt:

*   My prompt is successful because AI created `my_tool.py` to run the scraping and plotting steps in order. 
*   I run `my_tool.py` successfully and I can enter a search term and genertae its plot with one command.
*   Since I asked AI to keep `scraped_data.csv`, I checked the saved data and verified that the plot matched it.

----
**FINAL REFLECTION:** Review your work. Write a brief statement of what you might have done differently in hindsight, or defend why your work was a good approach.

... YOUR FINAL REFLECTIONS HERE ...
My approach works very well because I clearly described how I wanted the two existing programs to work together. Since I had already tested both scripts in Subtask 1, then I could just combine these tested scripts based on the scripts in Subtask 1, which really helped me complete this subtask with one prompt.
----
----

### NEW TASK: Improve the Tool

----
Another idea that aligns with this challenge:

> Right now, users have to restart the tool every time they want to try a different search term, which can get repetitive when exploring multiple terms. An improvement would be to ask users after each plot if they want to search for another term, so they can keep going until they are done.

----
Which improvement I chose to implement (put an X on the line):

___  The professor's example idea

_X_  My idea above

----
Text of my first prompt:

> Work in the directory `m02`. Update `my_tool.py` so that after generating a plot, it asks whether the user wants to search for another term. If the user says yes, repeat the search and plotting process with their new input. If the user says no, end the program. Reuse the existing functions from `trends_save.py` and `trends_plot.py`, and leave `my_tool.py` unchanged.

Reflections on success/failure of this prompt:

*   The prompt worked, but I realized that asking the AI to update `my_tool.py` would change the version I used for the previous exercise. I revised my prompt to request a separate script (`my_tool_v2.py`, see my next prompt), so I could preserve my earlier work. 

----
Text of my next prompt:

> Work in the directory `m02`. Create a new script called `my_tool_v2.py` based on `my_tool.py`. After generating a plot, ask whether the user wants to search for another term. If the user says yes, repeat the search and plotting process with their new input. If the user says no, end the program. Reuse the existing functions from `trends_save.py` and `trends_plot.py`, and leave `my_tool.py` unchanged.

Reflections on success/failure of this prompt:

*   My prompt is successful because I tested continuing with another search and exiting the program, and both options worked as expected.
*   I clearly explained when the tool should ask about another search, and described what should happen for both answers.
*   I also asked the AI to reuse the existing functions, making it clear how the new script should build on my previous work.

----
**FINAL REFLECTION:** Review your work. Write a brief statement of what you might have done differently in hindsight, or defend why your work was a good approach.

... YOUR FINAL REFLECTIONS HERE ...
My approach improved over two prompts, and they both work well. In the first, I asked the AI to update `my_tool.py` directly, but I then realized I wanted to preserve my earlier work. I revised the prompt to request `my_tool_v2.py` instead. This taught me to specify both the changes I want and which files should remain unchanged. 
----
----

### Final Questions

1.  In your own words, give names to the steps in the problem-solving process you followed.

    - Step1: we have to understand the problem/task, and if it involves several steps, we could divide it into smaller, manageable subtasks and work through them one at a time
    - Step2: we have to write a clear prompt that describes the changes we want
    - Step3: we have to read the AI generated codes to check whether it matches our request
    - Step4: we have to run the program and test whether the program works and produces the expected results
    - Step5: if something fails or we notice that AI doesn't fully follow the requirements, then we can have to refine the prompt and test again

2.  Which step do you find most challenging, and why?

    Writing a clear prompt is the most challenging part because I need to think through all my requirements before explaining them to the AI. For example, when working on the exercises above, my initial prompts were often too simple and left out important details. I had to reread the task instructions and review my prompts to identify what was missing and where I could provide clearer information and more specific direction.

3.  What two questions do you have about how Python expresses the tasks you might ask it to do?

    1) How does python call a function defined in another file?
    2) How does python control the order in which functions run?

----
----

### Other's Review

... YOU DO NOTHING HERE; ANOTHER STUDENT WILL COMPLETE THIS PART IN SECTION ...

**positive thoughts**I think your lab notebook clearly use the prompt to achieve the goal, especially liked how you noticed that directly modifying my_tool.py in the improvement task would overwrite your previous work, and then revised your prompt to create my_tool_v2.py instead. This is exactly what people will be facing on the daily basis when doing vibe coding. I also liked that you tested both continuing with another search and exiting the program.

**constructive criticism**One suggestion I have is to make some of the reflections more specific about the actual code changes made by the AI, rather than mainly describing whether the program worked.

**Suggestions** Give the prompt in a more clear way that tell the action of the LLM. Also keep consistancy of the overall prompting pipeline. 


### AI's Review

Your work shows a clear and thoughtful progression from making a small change to an existing program, to combining existing tools, and finally designing your own usability improvement. One thing that is particularly noteworthy is that you generally gave the AI specific context, including the directory, filenames, desired behavior, and which existing functions or files should be reused. This likely helped you get useful results with relatively few prompts.

Your work on the improvement task also demonstrates useful iteration. After initially asking the AI to modify my_tool.py, you realized that you wanted to preserve the earlier version and revised your approach by creating my_tool_v2.py. That is a good example of evaluating not only whether AI-generated code works, but also whether the implementation fits the way you want to organize your project. Your peer's observation about preserving a working version reinforces this strength.

For future work, one improvement would be to spend more time examining and documenting the actual code generated by the AI. Many of your reflections focus on whether the program successfully produced the expected result. You could go one step further by identifying specific Python structures the AI used, explaining what they do, and considering whether there are alternative implementations. This would help strengthen your ability to evaluate AI-generated code rather than relying primarily on successful execution.

Another area to improve is checking prompts for internal consistency before sending them. For example, your first improvement prompt asks the AI to update my_tool.py while also saying to leave my_tool.py unchanged. You successfully recognized and corrected the issue afterward, but reviewing the prompt against your requirements before sending it could avoid unnecessary iterations.

Overall, your notebook demonstrates a strong iterative workflow: understand the problem, formulate a prompt, review the result, test it, recognize issues, and refine the approach. Going forward, focusing more on why the generated Python code works—not only whether it works—would make this process even more valuable for developing your own programming skills.
