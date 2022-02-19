c.NotebookApp.kernel_spec_manager_class = 'environment_kernels.EnvironmentKernelSpecManager'
c.NotebookApp.iopub_data_rate_limit = 10000000000
# 2022-02-19 Dmitry Fedyuk https://www.upwork.com/fl/mage2pro
# 1) "Setup Jupiter Notebook": https://github.com/dmitry-ai/aws-gpu-2022-02-06/issues/2
# 2.1) https://jupyter-notebook.readthedocs.io/en/stable/public_server.html#using-let-s-encrypt
# 2.2) https://github.com/jupyter/notebook/blob/v6.4.8/docs/source/public_server.rst#using-lets-encrypt
c.NotebookApp.certfile = u'/etc/letsencrypt/live/aws.dmitry.ai/fullchain.pem'
c.NotebookApp.keyfile = u'/etc/letsencrypt/live/aws.dmitry.ai/privkey.pem'