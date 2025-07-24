# RashiClassifier - Sefer HaMitzvot Analysis Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

A Python-based platform for downloading, organizing, and analyzing the complete Sefer HaMitzvot (Book of Commandments) by Rashi from the Hebrew Wikisource. The project systematically downloads all 613 commandments (248 positive and 365 negative) along with supporting content, organizing them into a structured local library for study and analysis.

**Bonus**: This repository also serves as a learning environment for beginner coders to practice team development skills like writing tickets, opening pull requests, using TDD practices, and AI-first coding principles.

## 🎯 Project Goals

### Primary Objectives
- **Complete Text Access**: Download and organize the full Sefer HaMitzvot corpus
- **Structured Analysis**: Provide tools for studying Rashi's commentary and methodology
- **Research Platform**: Enable academic and religious study of the 613 commandments
- **Content Organization**: Create a searchable, well-structured local library

### Secondary Benefits
- **Learning Environment**: Practice modern development practices in a real-world context
- **Team Collaboration**: Learn Git workflows, TDD, and AI-assisted coding
- **Open Source Contribution**: Experience contributing to meaningful projects

## 🚀 Quick Start

### Prerequisites
```bash
pip install -r requirements.txt
```

### Basic Usage
1. **Generate the preparation file:**
   ```bash
   cd downloader
   python generate_prep_file.py
   ```

2. **Download the content:**
   ```bash
   python download_sefer_hamitzvot.py
   ```

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Content Structure](#-content-structure)
- [Analysis Tools](#-analysis-tools)
- [Getting Started](#-getting-started)
- [Learning Opportunities](#-learning-opportunities)
- [Contributing](#-contributing)
- [Technical Documentation](#-technical-documentation)
- [License](#-license)

## 📖 Project Overview

### What is Sefer HaMitzvot?
Sefer HaMitzvot (Book of Commandments) is Rashi's systematic enumeration and explanation of the 613 commandments found in the Torah. It serves as a fundamental text for understanding Jewish law and Rashi's interpretive methodology.

### What This Project Does
- **Downloads** the complete text from Hebrew Wikisource
- **Organizes** content into logical categories (positive/negative commandments, principles, etc.)
- **Provides** a foundation for analysis and study tools
- **Enables** research into Rashi's commentary patterns and structures

## 📁 Project Structure

**Core Modules:**
- `downloader/` - Content acquisition from Wikisource
- `analyzer/` - Text analysis and research tools (future)
- `content/` - Organized Sefer HaMitzvot corpus

**Documentation:**
- `TECHNICAL_DOCUMENTATION.md` - Implementation details
- `LEARNING_OBJECTIVES.md` - Learning goals (secondary)

## 🔍 Analysis Tools

### Current Capabilities
- **Content Download**: Complete Sefer HaMitzvot corpus
- **Structured Organization**: Logical categorization of commandments
- **Text Processing**: Clean, searchable Hebrew text files

### Planned Analysis Features
- **Text Analysis**: Pattern recognition in Rashi's commentary
- **Commandment Classification**: Automated categorization and tagging
- **Statistical Analysis**: Frequency and relationship analysis
- **Search and Query**: Advanced text search capabilities
- **Data Visualization**: Charts and graphs of commandment relationships

## 🛤️ Learning Opportunities

While the primary goal is Rashi analysis, this project also provides an excellent environment for learning modern development practices:

### For Beginner Coders
- **Git Workflow**: Practice branching, commits, and pull requests
- **Test-Driven Development**: Learn TDD with real features
- **AI-First Coding**: Use AI assistants for development
- **Team Collaboration**: Work with others through code reviews

### For Researchers
- **Data Processing**: Learn text analysis and NLP techniques
- **Academic Computing**: Practice research-oriented programming
- **Documentation**: Write clear, scholarly documentation

## 🤝 Contributing

We welcome contributions from both researchers and learners!

### For Researchers & Scholars
1. **Identify Analysis Needs**: What aspects of Rashi's work need study?
2. **Propose Features**: Suggest new analysis tools or capabilities
3. **Implement Analysis**: Build tools for text analysis and research
4. **Document Findings**: Share insights and research results

### For Learners
1. **Fork the repository** and clone it to your local machine
2. **Create a feature branch** for your work
3. **Write tests first** following TDD principles
4. **Implement your feature** with AI assistance if needed
5. **Open a pull request** with a clear description
6. **Respond to feedback** and iterate on your code

### Code of Conduct
- Be respectful and supportive of all contributors
- Provide constructive, helpful feedback
- Encourage questions and learning
- Celebrate progress and achievements

## 📚 Resources

### Essential Reading
- [TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md) - Technical implementation details
- [LEARNING_OBJECTIVES.md](LEARNING_OBJECTIVES.md) - Learning goals and exercises (secondary)
- [downloader/README.md](downloader/README.md) - Module-specific documentation

### Research Context
- **Sefer HaMitzvot**: Understanding Rashi's systematic approach to commandments
- **Rashi's Methodology**: Study of his commentary patterns and techniques
- **Jewish Law**: Context for the 613 commandments and their organization

## 🙏 Acknowledgments

- Hebrew Wikisource for hosting the Sefer HaMitzvot content
- Rashi (Rabbi Shlomo Yitzchaki) for the original work
- The open source community for the tools that made this project possible
- All contributors who help advance both research and learning goals