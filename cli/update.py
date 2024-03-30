from cli.write import Writer
from cli.viz import *

def analyze_all(data_path, save_dir) :
    viz_overall_num_of_bugs(data_path, save_dir)
    viz_detailed_list(data_path, save_dir)
    viz_num_of_found_bugs_per_program(data_path, save_dir)
    viz_num_of_tested_projects(data_path, save_dir)

def main(data_path, save_dir) :
    analyze_all(data_path, save_dir)
    writer = Writer()
    writer.dump()

if __name__ == "__main__" :
    import sys 
    data_path = sys.argv[1] if len(sys.argv) > 1 else "data/bugList-WingTecher.xlsx.xlsx"
    save_dir = sys.argv[2] if len(sys.argv) > 2 else "res"
    main(data_path, save_dir)