# Runs Prefect Agent, for deployment in Kubernetes. 
FROM prefecthq/prefect:2-python3.10
RUN prefect cloud login --key PREFECT_CLOUD_KEY --workspace noahskusabagmailcom/noah-github
CMD ["prefect", "agent", "start", "-q", "default"]
