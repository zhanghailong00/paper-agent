---
name: weekly-report
description: Generate structured weekly reports from your completed tasks, meeting notes, and other data. Format can be customized for sharing with your team or management.
description_for_model: This skill helps the user create a professional weekly report of their accomplishments, tasks, and plans based on their input. The generated report follows their organizational format preferences and can be customized for different audiences (team updates, management reporting, etc).
repository: local
contributing: none
tags:
  - productivity
  - reporting
  - work
  - management
model: claude-3-5-sonnet-20240620
menu_title: Create weekly report
menu_description: Generate a professional weekly report for your team or management
---

# Weekly Report Generator

This skill helps you create professional weekly reports of your accomplishments, tasks, and plans. The generated reports follow your organizational format preferences and can be customized for different audiences (team updates, management reporting, etc.).

## Basic Usage

```
/weekly-report
```

I'll guide you through creating your weekly report by asking for:
- The time period (e.g., "This week", "April 17-23, 2026")
- Your preferred report format
- The target audience
- Your key accomplishments
- Any challenges or blockers
- Your plans for next week

## Advanced Usage

You can provide some or all information upfront:

```
/weekly-report I completed the frontend redesign this week, fixed 3 critical bugs, and led the team retrospective. Next week I'll focus on the API integration. This is for my manager.
```

## Report Formats

The skill supports several standard report formats:

1. **Standard Format**
   - Accomplishments
   - In Progress Work
   - Blockers/Challenges
   - Next Week's Plans

2. **STAR Method**
   - Situation
   - Task
   - Action
   - Result

3. **Management Summary**
   - Executive Overview
   - Key Metrics
   - Team Highlights
   - Resource Needs

4. **Custom Format**
   - You can describe your preferred structure

## Tips for Effective Reports

- Be specific about accomplishments with measurable outcomes when possible
- Keep entries concise and focused
- Highlight impact rather than just activities
- For management reports, emphasize business value
- For team reports, include more technical details
- Include relevant metrics when available (e.g., "reduced load time by 40%")

## Examples

### Team Update Example

```
/weekly-report This week I completed the user authentication module refactoring, participated in 3 code reviews, and fixed the production database connection issue. I'm blocked on deploying to staging due to DevOps pipeline issues. Next week I'll focus on the new reporting feature. This is for my engineering team.
```

### Management Report Example

```
/weekly-report Period: April 17-23, 2026. Completed Q2 customer satisfaction analysis showing 12% improvement, trained 2 new team members on data pipelines, delivered executive dashboard ahead of schedule. Challenged by data quality issues in European region. Planning to start budget forecasting next week. Format: Management Summary for director level.
```