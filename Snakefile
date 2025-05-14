# Snakefile

# Define the output of each rule

rule clean_data:
    input:
        r"data/rse.xlsx"
    output:
        r"results/clean_data.xlsx"
    script:
        "python3 src/clean_data_cli.py --input {input} --output {output}"

rule data_preprocessing:
    input:
        r"results/clean_data.xlsx"
    output:
        r"results/processed_data.xlsx"
    script:
        "python3 src/data_preprocessing_cli.py --input {input} --output {output}"

rule compare_by_region_administrative_responses:
    input:
        r"data/rse.xlsx"
    script:
        "python3 src/administrative_responses/compare_by_region.py --input {input}"


rule describe_data_administrative_responses:
    input:
        r"results/processed_data.xlsx"
    script:
        "python3 src/administrative_responses/describe_data.py --input {input}"


rule plot_administrative_responses:
    input:
        r"results/processed_data.xlsx"
    script:
        "python3 src/administrative_responses/plot_administrative_responses.py --input {input}"