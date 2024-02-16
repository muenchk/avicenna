from typing import List

from isla.language import ISLaUnparser

from debugging_benchmark.calculator.calculator import CalculatorBenchmarkRepository
from debugging_benchmark.student_assignments import MiddleAssignmentBenchmarkRepository
from debugging_framework.benchmark import BenchmarkRepository, BenchmarkProgram

from avicenna import Avicenna


def main():

    repos: List[BenchmarkRepository] = [
        MiddleAssignmentBenchmarkRepository()
    ]

    subjects: List[BenchmarkProgram] = []
    for repo in repos:
        subjects_ = repo.build()
        subjects += subjects_

    print(f"Number of subjects: {len(subjects)}")

    for subject in subjects:
        param = subject.to_dict()

        param["top_n_relevant_features"] = 4

        avicenna = Avicenna(**param)
        diagnosis = avicenna.explain()
        if diagnosis:
            print(f"Final Diagnosis for {subject}")
            print(ISLaUnparser(diagnosis[0]).unparse())
            print(f"Avicenna calculated a precision: {diagnosis[1] * 100:.2f}% and recall {diagnosis[2] * 100:.2f}%")
        else:
            print(f"No diagnosis has been learned for {subject}!")


if __name__ == "__main__":
    main()