from prefect.infrastructure import KubernetesJob
from prefect.filesystems import GitHub
import os
from dotenv import load_dotenv
load_dotenv()

def github_storageBlock():
    storage_block = GitHub(
        repository = os.environ["REP_URL"],
        access_token =  os.environ["ACCESS_TOKEN"]  
    )
    storage_block.save("etl-kubernetes", overwrite = True)

def get_requirements():
    #This variable will contain all needed packages
    packages = ''
    with open('requirements.txt', 'r') as infile:
        packages = " ".join(infile)
    infile.close()
    packages = packages.strip()
    return packages


def main():
    
    packages = get_requirements()
    # breakpoint()
    github_storageBlock()
    k8s_job = KubernetesJob(
        image="prefecthq/prefect:2.0a11-python3.8",
        image_pull_policy="Always",
        env={"EXTRA_PIP_PACKAGES": packages},
    )

    k8s_job.save("k8s-flow", overwrite=True)


if  __name__ == "__main__":
    main()