# Runs Prefect Agent, for deployment in Kubernetes. 
FROM prefecthq/prefect:2-python3.10
COPY kubeconfig.yaml /root/.kube/config
ENV KUBECONFIG=/root/.kube/config
RUN prefect cloud login --key your_prefect_cloud_key --workspace noahskusabagmailcom/noah-github
CMD ["prefect", "agent", "start", "-q", "default"]
