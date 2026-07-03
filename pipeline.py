import subprocess
import sys
from datetime import datetime

def run_step(step_name, script_path):
    print("\n" + "="*60)
    print(f"{step_name}")
    print("="*60)

    start_time = datetime.now()

    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print("ERROR OCCURRED:")
        print(result.stderr)
        print(f"\nPipeline failed at: {step_name}")
        exit(1)

    end_time = datetime.now()
    print(f"Completed: {step_name}")
    print(f"Time taken: {end_time - start_time}")


def main():
    print("\n" + "#"*60)
    print("SALES DATA ETL PIPELINE STARTED")
    print("#"*60)

    run_step("STEP 1: Data Splitting", "scripts/split_data.py")

    run_step("STEP 2: Data Validation", "scripts/validation.py")

    run_step("STEP 3: Data Cleaning", "scripts/cleaning.py")

    run_step("STEP 4: Data Transformation", "scripts/transformation.py")

    run_step("STEP 5: Load to MySQL", "scripts/load_to_sql.py")

    print("\n" + "#"*60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("#"*60)


if __name__ == "__main__":
    main()