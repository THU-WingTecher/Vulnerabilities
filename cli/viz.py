import os
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Create a fancy plot
DATA_NAMES = ['CVE.md', 'CNVD.md', 'others.md', 'num_of_bug_per_projects.png', 'num_of_tested_projects.png', 'overall.png']
def df_to_markdown(df, sheet_name):
    # Limiting rows for demonstration
    markdown = f"### {sheet_name} Data\n"
    markdown += "| " + " | ".join(df.columns) + " |\n"
    markdown += "|-" + "-|-".join([""] * len(df.columns)) + "-|\n"
    for _, row in df.iterrows():
        markdown += "| " + " | ".join(str(value) for value in row) + " |\n"
    return markdown

def viz_num_of_found_bugs_per_program(data_path, save_dir) :
    all_sheets = pd.read_excel(data_path, sheet_name=None)
    all_data_df = pd.concat([sheet_df[['程序']] for sheet_df in all_sheets.values()])

    # Count the occurrences of each project
    project_counts = all_data_df['程序'].value_counts().reset_index()
    project_counts.columns = ['Project', 'Count']
    top_projects = project_counts.head(10)

    # Creating a fancy horizontal bar chart for the top projects
    plt.figure(figsize=(10, 8))
    sns.barplot(x='Count', y='Project', data=top_projects, palette='viridis')

    # Adding titles and labels with custom styling
    plt.title('Top 10 Tested Projects by Bug Counts', fontsize=16, fontweight='bold', color='#333')
    plt.xlabel('Bug Count', fontsize=14, color='#333')
    plt.ylabel('Project', fontsize=14, color='#333')

    # Customizing the plot for a fancy look
    sns.despine(left=True, bottom=True)
    plt.grid(axis='x', linestyle='--', color='grey', alpha=0.5)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    # Save the fancy plot as a PNG file
    plt.savefig(os.path.join(save_dir, "num_of_bug_per_projects.png"), dpi=300, bbox_inches='tight', facecolor='#f7f7f7')

def viz_num_of_tested_projects(data_path, save_dir) :
    all_sheets = pd.read_excel(data_path, sheet_name=None)
    all_data_df = pd.concat([sheet_df[['程序']] for sheet_df in all_sheets.values()])

    # Count the occurrences of each project
    project_counts = all_data_df['程序'].value_counts().reset_index()
    total_projects_tested = project_counts.shape[0]

    # Create a visualization highlighting the total number of projects tested
    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor('#f7f7f7')
    ax.axis('off')

    # Text for the total number of projects tested
    total_projects_text = f"{total_projects_tested}\nProjects Tested"

    # Custom font properties
    fontdict_total_projects = {'fontsize': 28, 'fontweight': 'bold', 'color': '#0077b6'}

    # Add text
    ax.text(0.5, 0.5, total_projects_text, fontdict=fontdict_total_projects, ha='center', va='center', transform=ax.transAxes)

    # Save the plot as a PNG file
    plt.savefig(os.path.join(save_dir, "num_of_tested_projects.png"), dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())

    plt.show()

def viz_detailed_list(data_path, save_dir) :
    all_sheets = pd.read_excel(data_path, sheet_name=None)
    markdown_tables = {sheet_name: df_to_markdown(sheet_df, sheet_name) for sheet_name, sheet_df in all_sheets.items()}
    for sheet_name, markdown_table in markdown_tables.items():
    # Save the Markdown table to a text file
        with open(os.path.join(save_dir, sheet_name+".md"), 'w') as file:
            file.write(markdown_table)

def viz_overall_num_of_bugs(data_path, save_dir):

    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_facecolor('#f7f7f7')
    ax.axis('off')

    all_sheets = pd.read_excel(data_path, sheet_name=None)
    bug_counts = {sheet_name: len(sheet_df) for sheet_name, sheet_df in all_sheets.items()}

    # Convert to DataFrame for visualization
    bug_counts_df = pd.DataFrame(list(bug_counts.items()), columns=['Category', 'Count'])

    total_bugs_found = bug_counts_df['Count'].sum()
    # Total bugs found
    total_bugs_text = f"{total_bugs_found} Bugs Found\n(CVE: {bug_counts['CVE']}, CNVD: {bug_counts['CNVD']}, Others: {bug_counts['others']})"
    # Custom font properties
    fontdict_header = {'fontsize': 24, 'fontweight': 'bold', 'color': '#ff5733'}
    fontdict_annotation = {'fontsize': 14, 'color': '#2c3e50'}

    # Custom font properties
    fontdict_header = {'fontsize': 20, 'fontweight': 'bold', 'color': '#ff5733'}
    fontdict_details = {'fontsize': 16, 'color': '#2c3e50'}
    # Add text with details
    ax.text(0.5, 0.55, total_bugs_text, fontdict=fontdict_header, ha='center', va='center', transform=ax.transAxes, wrap=True)
    # Save the plot as a PNG file for the updated fancy total bugs visualization
    plt.savefig(os.path.join(save_dir, "overall.png"), bbox_inches='tight', facecolor=fig.get_facecolor(), dpi=300)

viz_overall_num_of_bugs('data/bugList-WingTecher.xlsx', 'res')
viz_detailed_list('data/bugList-WingTecher.xlsx', 'res')