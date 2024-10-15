Here’s the updated prompt with post-task instructions for committing and optionally pushing the branch if requested:

---

**Directive and Guidance for Generating a Detailed JOB TASK List**

---

**Instructions for AI Assistant:**  
Use the information provided to generate a detailed JOB TASK List based on the user’s job request and project requirements. Follow the guidelines below to create a structured list of tasks with clear implementation steps and reporting instructions.

### Input Information:

1. **Project Name or Code**  
   - Example: "Dudoxx" or "DXX"

2. **Job Title**  
   - Example: "Content Review and Implementation"

3. **Date**  
   - Example: "October 15th, 2024"

4. **Job Request Description**  
   - Specific instructions from the user about what the job entails. Example: "Integrate enhanced content on all 'Learn More' pages using Bootstrap styling."

5. **Project Context and Paths**  
   - **Context**: Briefly summarize the project background and key requirements. Example: "The Vite project requires content and styling updates for consistency across all pages."
   - **Paths**: List project paths (e.g., Project Root, Pages Directory, Components Directory, Content Files Directory, etc.) for clarity on file locations.

6. **Additional Details**  
   For each of these points, default to **“No”** unless explicitly mentioned in the request:
   - **Existing File Structure or Naming Conventions**: If available, provide details on any file structure or naming patterns.
   - **Preferred Tone or Style for Content**: Specify if the job requires a particular tone or style in written content (e.g., technical, persuasive).
   - **Placeholder Specifications**: Indicate any specific dimensions or alignment needed for image or component placeholders.
   - **Testing or Review Requirements**: Outline any specific testing or review needs after task completion.
   - **Project Documentation Update Requirements**: Specify if the task requires documentation updates in project codebase files in addition to reporting.
   - **Push Branch on Completion**: If the user requests, add a post-task to push the branch to the remote repository after committing.

### Generate the JOB TASK List with the Following Structure:

1. **Job ID**  
   Create a unique identifier by combining the project name, job title, and date, formatted as `JOB_[PROJECT_NAME]_[JOB_TITLE]_[DATE]`.

2. **Objective**  
   Summarize the core objective of the job, reflecting the main tasks and goals, based on the **Job Request Description**.

3. **Prerequisite Task**  
   Include a Git setup step:
   - **If** the project is a Git repository, create a new branch from the current branch, naming it after the job ID (e.g., `JOB_[PROJECT_NAME]_[JOB_TITLE]_[DATE]`).
   - **If not**, skip this task.

4. **Task List**  
   Based on the job description, generate a list of tasks. For each task:
   - Assign a **Task ID** in the format `TASK_[JOB_ID]_T#`.
   - Provide a **Detailed Description**:
     - Explain the task, specifying files or components to update, layout or styling instructions, and any content-related directives.
     - **Documentation Requirements**: Specify output files for task documentation in the format `TASK_[TASK_ID]_[TASK_DESC].md`.
     - **Example Task** (Optional): Provide a sample if there are new elements or components to illustrate the layout.

5. **Post-Tasks**  
   Add post-tasks to commit and optionally push the branch:
   - **Commit the Branch**  
     - **Task ID**: `TASK_[JOB_ID]_COMMIT_BRANCH`
     - **Description**: After all tasks are complete, commit all changes in the created branch with a message summarizing the job, such as “Completed JOB_[PROJECT_NAME]_[JOB_TITLE]_[DATE].”
   
   - **Push the Branch (if requested)**  
     - **Task ID**: `TASK_[JOB_ID]_PUSH_BRANCH`
     - **Description**: If the user has requested a push, push the branch to the remote repository after committing.

6. **Reporting**  
   - Create a **reporting folder** named after the job ID, e.g., `JOB_[JOB_ID]`.
   - Save each task’s progress report within this folder, using the format `TASK_[TASK_ID]_[TASK_DESC].md`.
   - Create an **overall job progress report** in `JOB_[JOB_ID]/JOB_ID_PROGRESS.md`.

### Example Output Structure:

- **Job ID**: JOB_[PROJECT_NAME]_CONTENT_INTEGRATION_20241015
- **Objective**: "To populate each topic page and 'Learn More' section with cohesive, professional content, applying Bootstrap styling and consistent placeholders as required."
- **Prerequisite Task**: Create a New Git Branch
    - **Description**: Check if the project is a Git repository. If so, retrieve the current branch name, then create a new branch named `JOB_[PROJECT_NAME]_CONTENT_INTEGRATION_20241015`. Skip if no Git repository exists.
- **Task List**:
  - **Task 1**: Implement Enhanced Content for Home Page with ID `TASK_JOB_[PROJECT_NAME]_CONTENT_INTEGRATION_20241015_T01`
      - **Description**: Insert content from `home-content.md` into the Home page. Use Bootstrap components such as headers, text containers, and buttons for layout consistency. Include image placeholders as necessary.
      - **Documentation**: `TASK_JOB_[PROJECT_NAME]_CONTENT_INTEGRATION_20241015_T01_HOMEPAGE_IMPLEMENTATION.md`

  - **Task 2**: Review and Implement Content for Business Objectives Page with ID `TASK_JOB_[PROJECT_NAME]_CONTENT_INTEGRATION_20241015_T02`
      - **Description**: Integrate `business-objectives-content.md` using Bootstrap grids and card components. Ensure readability and add image placeholders as specified.
      - **Documentation**: `TASK_JOB_[PROJECT_NAME]_CONTENT_INTEGRATION_20241015_T02_BUSINESS_OBJECTIVES_IMPLEMENTATION.md`

- **Post-Tasks**:
   - **Commit the Branch**: `TASK_JOB_[PROJECT_NAME]_CONTENT_INTEGRATION_20241015_COMMIT_BRANCH`
      - **Description**: Commit all changes in the created branch with the message “Completed JOB_[PROJECT_NAME]_CONTENT_INTEGRATION_20241015.”
   - **Push the Branch** (if requested): `TASK_JOB_[PROJECT_NAME]_CONTENT_INTEGRATION_20241015_PUSH_BRANCH`
      - **Description**: Push the branch to the remote repository if the user has requested it.

- **Reporting**:
   - Create a folder named `JOB_[PROJECT_NAME]_CONTENT_INTEGRATION_20241015`.
   - Save individual task progress reports as `TASK_[TASK_ID]_[TASK_DESC].md`.
   - Save a job progress summary as `JOB_[PROJECT_NAME]_CONTENT_INTEGRATION_20241015/JOB_ID_PROGRESS.md`.

This prompt ensures comprehensive task management, including setup, detailed implementation, reporting, and Git version control as needed.