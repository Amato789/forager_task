<h1>Test task for Forager.ai</h1>
<p align="left">
   <img src="https://img.shields.io/badge/Python-3.11-yellow" alt="Python Version">
   <img src="https://img.shields.io/badge/Style-wemake-blue" alt="Beautiful Soup Version">
   <img src="https://img.shields.io/badge/requests-2.31.0-blue" alt="Requests Version">
</p>

## About

Test task for the Junior Python Developer position.

## Examples of How To Use
1. Install module:

    `pip install forager-task`

2. Create a request with the desired email address:

    ```python
    import forager_task

    result = forager_task.handle_command(
        command='email_verification', 
        command_args={'email': 'YOUR_EMAIL'}, 
        save_strategy='to_file'
        api_key='YOUR_API_KEY_FROM_HUNTER.IO'
    )
    print(result)
    ```
3. Enjoy the result ).
