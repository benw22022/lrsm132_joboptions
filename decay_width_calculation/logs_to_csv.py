"""
Log files to csv
_______________________________________________
Convert logs files from MadGraph Generation to
csv of parameters and decay widths
"""

import argparse
import glob
import pandas as pd
import csv

def read_log_file(logfile):

    param_dict = {"MW2": None,
                  "MN1": None, 
                  "MN2": None, 
                  "MN3": None, 
                  "VKe": None,
                  "VKmu": None,
                  "VKta": None,
                  "tanb": None,
                  "WW2": None,
                  "WN4": None,
                  "WN5": None,
                  "WN6": None,
                  }

    with open(logfile, 'r') as file:
        reached_eof = False
        for line in file:
            if "Summary of results:" in line:
                reached_eof = True
            if reached_eof:
                for key in param_dict:
                    if f"{key} = " in line:
                        value = line.split("=")[-1]
                        try:
                            param_dict[key] = float(value)
                        except ValueError:
                            if '+0j' in value:
                                param_dict[key] = value.replace("(", "").replace(")", "").replace("+0j", "")
                            else:
                                print(f"ERROR: In {file} -- Cannot convert {key} = {value} to float")
                                return 1

    return param_dict

def add_dicts(list_of_dicts):

    param_dict = {"MW2": [],
                "MN1":  [], 
                "MN2":  [], 
                "MN3":  [], 
                "VKe": [],
                "VKmu": [],
                "VKta": [],
                "tanb": [],
                "WW2": [],
                "WN4": [],
                "WN5": [],
                "WN6": [],
                }

    for key in list_of_dicts[0]:
        for i in range(0, len(list_of_dicts)):
            param_dict[key].append(list_of_dicts[i][key])

    return param_dict

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Log file directory", type=str)
    args = parser.parse_args()

    log_files = glob.glob(f"{args.dir}/*.log")

    print(log_files)

    if len(log_files) == 0:
        print("ERROR: No Log Files Found")
        return 1

    param_dicts = []

    for log in log_files:
        param_dicts.append(read_log_file(log))
    
    param_dicts = add_dicts(param_dicts)

    print(param_dicts)

    param_df = pd.DataFrame.from_dict(param_dicts)
    param_df.to_csv(f"{args.dir}/widths.csv", index=False)

    
if __name__ == "__main__":
    main()

