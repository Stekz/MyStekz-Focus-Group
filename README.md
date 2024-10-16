# MystekzFocusGroup Crew

Welcome to the MystekzFocusGroup Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry.

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and install them by using the CLI command:
```bash
poetry install
poetry run crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/mystekz_focus_group/config/agents.yaml` to define your agents
- Modify `src/mystekz_focus_group/config/tasks.yaml` to define your tasks
- Modify `src/mystekz_focus_group/crew.py` to add your own logic, tools and specific args
- Modify `src/mystekz_focus_group/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ poetry run chat
```

To enable the watcher, run:

```bash
$ poetry run chat_watch
```

This command starts up a chanlit chat which will use the focus group for any idea you throw at them. 

**NOTE**: The Chainlit app may not always show the response. The results and all intermediate steps taken are printed in the console.
