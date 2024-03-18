# [Install Databricks CLI](https://docs.databricks.com/en/dev-tools/cli/index.html)

```shell
brew tap databricks/tap
brew install databricks
```

## [Authentication for the Databricks CLI](https://docs.databricks.com/en/dev-tools/cli/authentication.html)

1. Use the Databricks CLI to run the following command:
    ```shell
    databricks configure
    ```
2. Databricks Host:
    ```
    https://dbc-a1b2345c-d6e7.cloud.databricks.com
    ```
3. Personal Access Token.
   Sau khi token, sẽ tạo ra folder `.databrickscfg` tại `~/.databrickscfg`
4. 
    ```shell
    databricks clusters list --profile <configuration-profile-name>.
    ```
## Configure Databricks
```shell
databricks auth login --configure-cluster --host <workspace-url>
```