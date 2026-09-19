## My Lab Notebook for CS1066 PSet #1

INSERT-YOUR-NAME

INSERT-YOUR-VIDEO-LINK (after completing this assignment)

----Zifan Zhao
---- https://youtu.be/hlBsRpV2kT0

### SUBTASK #1: Prompt for the Search Term

----
Text of my first prompt:

> Modify trends_save.py so that the user is prompted to enter a search term or phrase whenever they are using the program. Do not change the rest of the program's behavior.

Reflections on success/failure of this prompt:

*   WRITE-BULLET-LIST-OF-THOUGHTS
- it suggests me to have an input function with "search a term or phase", and I think it fits the need from my prompt. 
- There is no huge changes of the script and exactly excute what I told it to do. 

----
Text of my next prompt:

> it is not working properly, debug it

Reflections on success/failure of this prompt:

*   WRITE-BULLET-LIST-OF-THOUGHTS
- It rebuged the successfully and the problem is related to the environment
- it also mentioned I have to use terminal to run the script instead of the run botton on the top
----


----
**FINAL REFLECTION:** Review your work. Write a brief statement of what you might have done differently in hindsight, or defend why your work was a good approach.

... YOUR FINAL REFLECTIONS HERE ...
- I first asked a very concret request to the llm and the output it gives me is solid and accurate. However because there are some virtual environment issues, I have to debug it. Next time I will try to make sure the environment looks good and that will make the entire workflow more smooth. 
----
----

### SUBTASK #2: Just One Tool

----
Text of my first prompt:

- Create a new Python script (called `my_tool.py`) that combines the running of `trends_save.py` and `trends_plot.py`.Do not create any files that are not needed 

Reflections on success/failure of this prompt:

*   WRITE-BULLET-LIST-OF-THOUGHTS
-Everything goes well on this prompt to fit the need, one improvement could be make the prompt cleaner and double check. 
----
Text of my next prompt:

> is there any intermediate files that are not needed? make sure everything is clear and runnable. 

Reflections on success/failure of this prompt:

*   WRITE-BULLET-LIST-OF-THOUGHTS
Everything is up to date. 

----

----
**FINAL REFLECTION:** Review your work. Write a brief statement of what you might have done differently in hindsight, or defend why your work was a good approach.


----I think my approach worked well because I reused the existing scripts instead of asking the AI to rewrite everything from scratch. I also considered whether unnecessary intermediate files were being created. In hindsight, I could have made my second prompt more specific instead of simply asking whether everything was clear and runnable.
----

### NEW TASK: Improve the Tool

----
Another idea that aligns with this challenge:

> INSERT-DESCRIPTION-OF-THE-IDEA

----
Which improvement I chose to implement (put an X on the line):

___  The professor's example idea
X I chose to implement the example improvement of automatically naming the plot file based on the search term. I chose this because it directly prevents previous plots from being overwritten and makes it easier for users to identify and compare their results.
___  My idea above
 Currently, the user has to restart the tool every time they want to investigate a different search term. This can become repetitive when comparing several topics. I would improve the tool by asking the user whether they want to search for another term after each plot is generated. This would allow the user to explore multiple questions in one session without repeatedly restarting the program.

----
Text of my first prompt:

> Improve my_tool.py so that the output plot is automatically given a meaningful filename based on the user's search term instead of always using the same filename. Tell the user the name of the saved plot file, and only ask the user what to do if a file with that name already exists.

Reflections on success/failure of this prompt:

*   WRITE-BULLET-LIST-OF-THOUGHTS
- The AI changed the tool so that the output filename is based on the search term and tells the user where the plot was saved. It also checks whether a file with the same name already exists before continuing. This matched the improvement I chose, so no further edits were needed.





----
**FINAL REFLECTION:** Review your work. Write a brief statement of what you might have done differently in hindsight, or defend why your work was a good approach.


----I think this is like a real world vibe coding pipeline. Because I broke down the question into several pieces and iterate several times when needed. Each time I will review the output of the AI to make sure it generated things that I exactly want. Also, I make sure that the prompt I gave to the LLM is accurate but not some general questions. When there is a problem I just let the LLM to debug it. 
----

### Final Questions

1.  In your own words, give names to the steps in the problem-solving process you followed.

    I would describe the steps as: understand the problem, break down, plannin phase, prompting phase, AI coding implementation, review suggested code, testing, and Quality check.

2.  Which step do you find most challenging, and why?

    I think prompting phase is most chanllenging becasue I have to make sure giving the LLM accurate command to let it excute and output things that is exactly what I want. 

3.  What two questions do you have about how Python expresses the tasks you might ask it to do?

    YOUR-ANSWER-HERE

----How does Python decide which code runs when one Python file imports another file?
----When should I use functions to organize a program instead of putting the code directly in the main script?

### Other's Review

I liked that your first prompt clearly asked for user input while keeping the rest of the program‘s behavior unchanged. I think this was an important detail because it helps prevent the AI from making unnecessary changes, and it was something I didn‘t think about when writing my own prompt. I also liked how you broke the overall task into smaller steps and reviewed the AI’s output after each step.

One thing I learned from comparing our approaches is that we chose different improvements for the new task. I implemented repeated searches in one session, and you focused on automatically naming plot files based on the search term and handling existing filenames. I think these two could work well together, since users could run several searches and still easily identify and keep track of their plots.

One suggestion is to provide more context in some of your prompts. For example, specifying the working directory could make it clearer where the AI should make changes, and instead of simply saying “debug it”, including the error or unexpected behavior could help the AI identify the problem more efficiently. For Subtask 2, it may also help to clarify which intermediate files are unnecessary. I chose to keep `scraped_data.csv` so I could compare the saved data with the plot and check the result.

Baoyue Xing

----
----

### AI's Review

Your work shows a strong progression from simple code changes to workflow design:

- You started with a precise constraint: add a search prompt while preserving existing behavior. That constraint likely prevented unnecessary rewrites.
- You decomposed the assignment into manageable subtasks and iterated instead of asking for one large solution.
- You reused existing scripts for `my_tool.py`, which was a good engineering choice because it reduced duplication and limited the risk of changing working code.
- You selected an improvement with clear user value: search-based filenames prevent plots from being overwritten and make results easier to compare.
- You recognized that AI output still needs review, debugging, and testing. Both the peer feedback and AI review independently identified this as a strength.
- Your questions about imports and functions show that you are beginning to connect AI-generated code with Python’s underlying concepts.

The main weakness is that some reflections claim success without documenting how you verified it. For example, “everything is up to date” and “no further edits were needed” would be stronger if you described specific tests: which command you ran, what input you provided, what file was created, and how you checked overwrite behavior.

For future work, I would suggest:

1. Make debugging prompts evidence-based. Instead of “debug it,” include the exact error message, command used, expected result, actual result, and relevant environment details.
2. State the working directory and file relationships explicitly. For example: “From `m02`, modify `my_tool.py`, which imports or runs `trends_save.py` and `trends_plot.py`.”
3. Define acceptance criteria before prompting. For the filename improvement, specify how spaces, punctuation, and repeated searches should be handled, and what should happen when a filename already exists.
4. Ask the AI to explain its changes briefly, especially when it modifies imports, functions, file paths, or subprocess behavior. This helps you learn rather than only evaluate whether the program runs.
5. Test edge cases deliberately: an empty search term, a search term containing spaces or punctuation, two identical searches, a pre-existing output file, and a failed data download.

The most important improvement is to treat each prompt as a small specification: provide context, constraints, expected behavior, and a testable definition of success. Your existing workflow is sound; adding stronger evidence and edge-case testing would make it much more reliable and demonstrate deeper understanding.
