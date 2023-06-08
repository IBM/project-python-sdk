# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Examples for ProjectV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from project.project_v1 import *

#
# This file provides an example of how to use the project service.
#
# The following configuration properties are assumed to be defined:
# PROJECT_URL=<service base url>
# PROJECT_AUTH_TYPE=iam
# PROJECT_APIKEY=<IAM apikey>
# PROJECT_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'project_v1.env'

project_service = None

config = None

# Variables to hold link values
config_id_link = None
project_id_link = None


##############################################################################
# Start of Examples for Service: ProjectV1
##############################################################################
# region
class TestProjectV1Examples:
    """
    Example Test Class for ProjectV1
    """

    @classmethod
    def setup_class(cls):
        global project_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            project_service = ProjectV1.new_instance(
            )

            # end-common
            assert project_service is not None

            # Load the configuration
            global config
            config = read_external_sources(ProjectV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_project_example(self):
        """
        create_project request example
        """
        try:
            global project_id_link
            print('\ncreate_project() result:')
            # begin-create_project

            project_config_prototype_model = {
                'name': 'common-variables',
                'locator_id': '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global',
            }

            response = project_service.create_project(
                resource_group='Default',
                location='us-south',
                name='acme-microservice',
                description='A microservice to deploy on top of ACME infrastructure.',
                configs=[project_config_prototype_model],
            )
            project = response.get_result()

            print(json.dumps(project, indent=2))

            # end-create_project

            project_id_link = project['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_config_example(self):
        """
        create_config request example
        """
        try:
            global config_id_link
            print('\ncreate_config() result:')
            # begin-create_config

            project_config_input_variable_model = {
                'name': 'account_id',
                'value': '$configs[].name[\"account-stage\"].input.account_id',
            }

            project_config_setting_collection_model = {
                'name': 'IBMCLOUD_TOOLCHAIN_ENDPOINT',
                'value': 'https://api.us-south.devops.dev.cloud.ibm.com',
            }

            response = project_service.create_config(
                project_id=project_id_link,
                name='env-stage',
                locator_id='1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global',
                labels=['env:stage', 'governance:test', 'build:0'],
                description='Stage environment configuration, which includes services common to all the environment regions. There must be a blueprint configuring all the services common to the stage regions. It is a terraform_template type of configuration that points to a Github repo hosting the terraform modules that can be deployed by a Schematics Workspace.',
                input=[project_config_input_variable_model],
                setting=[project_config_setting_collection_model],
            )
            project_config_get_response = response.get_result()

            print(json.dumps(project_config_get_response, indent=2))

            # end-create_config

            config_id_link = project_config_get_response['id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_projects_example(self):
        """
        list_projects request example
        """
        try:
            print('\nlist_projects() result:')
            # begin-list_projects

            all_results = []
            pager = ProjectsPager(
                client=project_service,
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_projects
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_project_example(self):
        """
        get_project request example
        """
        try:
            print('\nget_project() result:')
            # begin-get_project

            response = project_service.get_project(
                id=project_id_link,
            )
            project_summary = response.get_result()

            print(json.dumps(project_summary, indent=2))

            # end-get_project

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_configs_example(self):
        """
        list_configs request example
        """
        try:
            print('\nlist_configs() result:')
            # begin-list_configs

            response = project_service.list_configs(
                project_id=project_id_link,
            )
            project_config_collection = response.get_result()

            print(json.dumps(project_config_collection, indent=2))

            # end-list_configs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_config_example(self):
        """
        get_config request example
        """
        try:
            print('\nget_config() result:')
            # begin-get_config

            response = project_service.get_config(
                project_id=project_id_link,
                id=config_id_link,
            )
            project_config_get_response = response.get_result()

            print(json.dumps(project_config_get_response, indent=2))

            # end-get_config

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_config_example(self):
        """
        update_config request example
        """
        try:
            print('\nupdate_config() result:')
            # begin-update_config

            project_config_input_variable_model = {
                'name': 'account_id',
                'value': '$configs[].name[\"account-stage\"].input.account_id',
            }

            response = project_service.update_config(
                project_id=project_id_link,
                id=config_id_link,
                input=[project_config_input_variable_model],
            )
            project_config_get_response = response.get_result()

            print(json.dumps(project_config_get_response, indent=2))

            # end-update_config

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_approve_example(self):
        """
        approve request example
        """
        try:
            print('\napprove() result:')
            # begin-approve

            response = project_service.approve(
                project_id=project_id_link,
                id=config_id_link,
                comment='Approving the changes',
            )
            project_config_get_response = response.get_result()

            print(json.dumps(project_config_get_response, indent=2))

            # end-approve

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_check_config_example(self):
        """
        check_config request example
        """
        try:
            print('\ncheck_config() result:')
            # begin-check_config

            response = project_service.check_config(
                project_id=project_id_link,
                id=config_id_link,
            )
            project_config_get_response = response.get_result()

            print(json.dumps(project_config_get_response, indent=2))

            # end-check_config

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_install_config_example(self):
        """
        install_config request example
        """
        try:
            print('\ninstall_config() result:')
            # begin-install_config

            response = project_service.install_config(
                project_id=project_id_link,
                id=config_id_link,
            )
            project_config_get_response = response.get_result()

            print(json.dumps(project_config_get_response, indent=2))

            # end-install_config

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_uninstall_config_example(self):
        """
        uninstall_config request example
        """
        try:
            # begin-uninstall_config

            response = project_service.uninstall_config(
                project_id=project_id_link,
                id=config_id_link,
            )

            # end-uninstall_config
            print('\nuninstall_config() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_config_drafts_example(self):
        """
        list_config_drafts request example
        """
        try:
            print('\nlist_config_drafts() result:')
            # begin-list_config_drafts

            response = project_service.list_config_drafts(
                project_id=project_id_link,
                config_id='testString',
            )
            project_config_draft_summary_collection = response.get_result()

            print(json.dumps(project_config_draft_summary_collection, indent=2))

            # end-list_config_drafts

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_config_draft_example(self):
        """
        get_config_draft request example
        """
        try:
            print('\nget_config_draft() result:')
            # begin-get_config_draft

            response = project_service.get_config_draft(
                project_id=project_id_link,
                config_id='testString',
                version=38,
            )
            project_config_draft = response.get_result()

            print(json.dumps(project_config_draft, indent=2))

            # end-get_config_draft

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_config_example(self):
        """
        delete_config request example
        """
        try:
            print('\ndelete_config() result:')
            # begin-delete_config

            response = project_service.delete_config(
                project_id=project_id_link,
                id=config_id_link,
            )
            project_config_delete = response.get_result()

            print(json.dumps(project_config_delete, indent=2))

            # end-delete_config

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_project_example(self):
        """
        delete_project request example
        """
        try:
            # begin-delete_project

            response = project_service.delete_project(
                id=project_id_link,
            )

            # end-delete_project
            print('\ndelete_project() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: ProjectV1
##############################################################################
