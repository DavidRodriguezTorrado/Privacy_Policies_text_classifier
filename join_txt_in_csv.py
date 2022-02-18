import pandas as pd
import subprocess

output_files = subprocess.check_output(['ls', './Validation/landing_pages']).decode('utf-8')
output_policies = subprocess.check_output(['ls', './Validation/policies']).decode('utf-8')

apps_files = output_files.split('\n')
policies = output_policies.split('\n')

df_policies = pd.DataFrame()
df_policies['apk'] = ''
df_policies['text'] = ''
i = 0
for app in policies:
    if app != '':
        app_name = app[:-4]
        df_policies.at[i, 'apk'] = app_name
        f = open('./Validation/policies/{}'.format(app), 'r')
        df_policies.at[i, 'text'] = f.read()
        f.close()
        i = i+1

df_apps = pd.DataFrame()
df_apps['apk'] = ''
df_apps['text'] = ''
i = 0
for app in apps_files:
    if app != '':
        app_name = app[:-4]
        df_apps.at[i, 'apk'] = app_name
        f = open('./Validation/landing_pages/{}'.format(app), 'r')
        df_apps.at[i, 'text'] = f.read()
        f.close()
        i = i+1

df_final = pd.concat([df_policies, df_apps])
df_final.to_csv('./Validation/validation_annotated.csv', index=False)