# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.
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
from ibm_project_sdk.project_v1 import *

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

            project_service = ProjectV1.new_instance()

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

            project_prototype_definition_model = {
                'name': 'acme-microservice',
                'description': 'A microservice to deploy on top of ACME infrastructure.',
            }

            response = project_service.create_project(
                definition=project_prototype_definition_model,
                location='us-south',
                resource_group='Default',
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

            project_config_prototype_definition_block_model = {
                'name': 'env-stage',
                'description': 'Stage environment configuration.',
                'inputs': {
                    'account_id': 'account_id',
                    'resource_group': 'stage',
                    'access_tags': ['env:stage'],
                    'logdna_name': 'LogDNA_stage_service',
                    'sysdig_name': 'SysDig_stage_service',
                },
                'settings': {'IBMCLOUD_TOOLCHAIN_ENDPOINT': 'https://api.us-south.devops.dev.cloud.ibm.com'},
                'locator_id': '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global',
            }

            response = project_service.create_config(
                project_id=project_id_link,
                definition=project_config_prototype_definition_block_model,
            )
            project_config = response.get_result()

            print(json.dumps(project_config, indent=2))

            # end-create_config

            config_id_link = project_config['id']
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
            project = response.get_result()

            print(json.dumps(project, indent=2))

            # end-get_project

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_project_example(self):
        """
        update_project request example
        """
        try:
            print('\nupdate_project() result:')
            # begin-update_project

            project_patch_definition_block_model = {
                'name': 'acme-microservice',
                'description': 'A microservice to deploy on top of ACME infrastructure.',
            }

            response = project_service.update_project(
                id=project_id_link,
                definition=project_patch_definition_block_model,
            )
            project = response.get_result()

            print(json.dumps(project, indent=2))

            # end-update_project

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_project_environment_example(self):
        """
        create_project_environment request example
        """
        try:
            print('\ncreate_project_environment() result:')
            # begin-create_project_environment

            project_config_auth_model = {
                'method': 'api_key',
                'api_key': 'TbcdlprpFODhkpns9e0daOWnAwd2tXwSYtPn8rpEd8d9',
            }

            project_compliance_profile_model = {
                'id': 'some-profile-id',
                'instance_id': 'some-instance-id',
                'instance_location': 'us-south',
                'attachment_id': 'some-attachment-id',
                'profile_name': 'some-profile-name',
            }

            environment_definition_required_properties_model = {
                'name': 'development',
                'description': 'The environment \'development\'',
                'authorizations': project_config_auth_model,
                'inputs': {'resource_group': 'stage', 'region': 'us-south'},
                'compliance_profile': project_compliance_profile_model,
            }

            response = project_service.create_project_environment(
                project_id=project_id_link,
                definition=environment_definition_required_properties_model,
            )
            environment = response.get_result()

            print(json.dumps(environment, indent=2))

            # end-create_project_environment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_project_environments_example(self):
        """
        list_project_environments request example
        """
        try:
            print('\nlist_project_environments() result:')
            # begin-list_project_environments

            response = project_service.list_project_environments(
                project_id=project_id_link,
            )
            environment_collection = response.get_result()

            print(json.dumps(environment_collection, indent=2))

            # end-list_project_environments

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_project_environment_example(self):
        """
        get_project_environment request example
        """
        try:
            print('\nget_project_environment() result:')
            # begin-get_project_environment

            response = project_service.get_project_environment(
                project_id=project_id_link,
                id=project_id_link,
            )
            environment = response.get_result()

            print(json.dumps(environment, indent=2))

            # end-get_project_environment

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_project_environment_example(self):
        """
        update_project_environment request example
        """
        try:
            print('\nupdate_project_environment() result:')
            # begin-update_project_environment

            project_config_auth_model = {
                'method': 'api_key',
                'api_key': 'TbcdlprpFODhkpns9e0daOWnAwd2tXwSYtPn8rpEd8d9',
            }

            project_compliance_profile_model = {
                'id': 'some-profile-id',
                'instance_id': 'some-instance-id',
                'instance_location': 'us-south',
                'attachment_id': 'some-attachment-id',
                'profile_name': 'some-profile-name',
            }

            environment_definition_properties_model = {
                'name': 'development',
                'description': 'The environment \'development\'',
                'authorizations': project_config_auth_model,
                'inputs': {'resource_group': 'stage', 'region': 'us-south'},
                'compliance_profile': project_compliance_profile_model,
            }

            response = project_service.update_project_environment(
                project_id=project_id_link,
                id=project_id_link,
                definition=environment_definition_properties_model,
            )
            environment = response.get_result()

            print(json.dumps(environment, indent=2))

            # end-update_project_environment

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
            project_config = response.get_result()

            print(json.dumps(project_config, indent=2))

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

            project_config_patch_definition_block_model = {
                'name': 'env-stage',
                'inputs': {
                    'account_id': 'account_id',
                    'resource_group': 'stage',
                    'access_tags': ['env:stage'],
                    'logdna_name': 'LogDNA_stage_service',
                    'sysdig_name': 'SysDig_stage_service',
                },
            }

            response = project_service.update_config(
                project_id=project_id_link,
                id=config_id_link,
                definition=project_config_patch_definition_block_model,
            )
            project_config = response.get_result()

            print(json.dumps(project_config, indent=2))

            # end-update_config

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_force_approve_example(self):
        """
        force_approve request example
        """
        try:
            print('\nforce_approve() result:')
            # begin-force_approve

            response = project_service.force_approve(
                project_id=project_id_link,
                id=config_id_link,
                comment='Approving the changes',
            )
            project_config_version = response.get_result()

            print(json.dumps(project_config_version, indent=2))

            # end-force_approve

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
            project_config_version = response.get_result()

            print(json.dumps(project_config_version, indent=2))

            # end-approve

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_validate_config_example(self):
        """
        validate_config request example
        """
        try:
            print('\nvalidate_config() result:')
            # begin-validate_config

            response = project_service.validate_config(
                project_id=project_id_link,
                id=config_id_link,
            )
            project_config_version = response.get_result()

            print(json.dumps(project_config_version, indent=2))

            # end-validate_config

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_deploy_config_example(self):
        """
        deploy_config request example
        """
        try:
            print('\ndeploy_config() result:')
            # begin-deploy_config

            response = project_service.deploy_config(
                project_id=project_id_link,
                id=config_id_link,
            )
            project_config_version = response.get_result()

            print(json.dumps(project_config_version, indent=2))

            # end-deploy_config

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_undeploy_config_example(self):
        """
        undeploy_config request example
        """
        try:
            # begin-undeploy_config

            response = project_service.undeploy_config(
                project_id=project_id_link,
                id=config_id_link,
            )

            # end-undeploy_config
            print('\nundeploy_config() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_sync_config_example(self):
        """
        sync_config request example
        """
        try:
            # begin-sync_config

            schematics_workspace_model = {
                'workspace_crn': 'crn:v1:staging:public:schematics:us-south:a/38acaf4469814090a4e675dc0c317a0d:95ad49de-ab96-4e7d-a08c-45c38aa448e6:workspace:us-south.workspace.service.e0106139',
            }

            response = project_service.sync_config(
                project_id=project_id_link,
                id=config_id_link,
                schematics=schematics_workspace_model,
            )

            # end-sync_config
            print('\nsync_config() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_config_resources_example(self):
        """
        list_config_resources request example
        """
        try:
            print('\nlist_config_resources() result:')
            # begin-list_config_resources

            response = project_service.list_config_resources(
                project_id=project_id_link,
                id=config_id_link,
            )
            project_config_resource_collection = response.get_result()

            print(json.dumps(project_config_resource_collection, indent=2))

            # end-list_config_resources

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_config_versions_example(self):
        """
        list_config_versions request example
        """
        try:
            print('\nlist_config_versions() result:')
            # begin-list_config_versions

            response = project_service.list_config_versions(
                project_id=project_id_link,
                id=config_id_link,
            )
            project_config_version_summary_collection = response.get_result()

            print(json.dumps(project_config_version_summary_collection, indent=2))

            # end-list_config_versions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_config_version_example(self):
        """
        get_config_version request example
        """
        try:
            print('\nget_config_version() result:')
            # begin-get_config_version

            response = project_service.get_config_version(
                project_id=project_id_link,
                id=config_id_link,
                version=38,
            )
            project_config_version = response.get_result()

            print(json.dumps(project_config_version, indent=2))

            # end-get_config_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_project_environment_example(self):
        """
        delete_project_environment request example
        """
        try:
            print('\ndelete_project_environment() result:')
            # begin-delete_project_environment

            response = project_service.delete_project_environment(
                project_id=project_id_link,
                id=project_id_link,
            )
            environment_delete_response = response.get_result()

            print(json.dumps(environment_delete_response, indent=2))

            # end-delete_project_environment

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
    def test_delete_config_version_example(self):
        """
        delete_config_version request example
        """
        try:
            print('\ndelete_config_version() result:')
            # begin-delete_config_version

            response = project_service.delete_config_version(
                project_id=project_id_link,
                id=config_id_link,
                version=38,
            )
            project_config_delete = response.get_result()

            print(json.dumps(project_config_delete, indent=2))

            # end-delete_config_version

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
