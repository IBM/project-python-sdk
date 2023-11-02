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
Integration Tests for ProjectV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from project.project_v1 import *

# Config file name
config_file = 'project_v1.env'

# Variables to hold link values
config_id_link = None
project_id_link = None


class TestProjectV1:
    """
    Integration Test Class for ProjectV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.project_service = ProjectV1.new_instance(
            )
            assert cls.project_service is not None

            cls.config = read_external_sources(ProjectV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.project_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_project(self):
        global project_id_link

        # Construct a dict representation of a ProjectPrototypeDefinition model
        project_prototype_definition_model = {
            'name': 'acme-microservice',
            'description': 'A microservice to deploy on top of ACME infrastructure.',
            'destroy_on_delete': True,
        }
        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile_id': 'testString',
            'method': 'api_key',
            'api_key': 'testString',
        }
        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {
            'id': 'testString',
            'instance_id': 'testString',
            'instance_location': 'testString',
            'attachment_id': 'testString',
            'profile_name': 'testString',
        }
        # Construct a dict representation of a InputVariable model
        input_variable_model = {
            'foo': 'testString',
        }
        # Construct a dict representation of a ProjectConfigSetting model
        project_config_setting_model = {
            'foo': 'testString',
        }
        # Construct a dict representation of a ProjectConfigPrototypeDefinitionBlock model
        project_config_prototype_definition_block_model = {
            'name': 'testString',
            'description': 'testString',
            'labels': ['testString'],
            'environment': 'testString',
            'authorizations': project_config_auth_model,
            'compliance_profile': project_compliance_profile_model,
            'locator_id': 'testString',
            'inputs': input_variable_model,
            'settings': project_config_setting_model,
        }
        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {
            'workspace_crn': 'testString',
        }
        # Construct a dict representation of a ProjectConfigPrototype model
        project_config_prototype_model = {
            'definition': project_config_prototype_definition_block_model,
            'schematics': schematics_workspace_model,
        }

        response = self.project_service.create_project(
            definition=project_prototype_definition_model,
            location='us-south',
            resource_group='Default',
            configs=[project_config_prototype_model],
        )

        assert response.get_status_code() == 201
        project = response.get_result()
        assert project is not None

        project_id_link = project['id']

    @needscredentials
    def test_create_config(self):
        global config_id_link

        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile_id': 'testString',
            'method': 'api_key',
            'api_key': 'testString',
        }
        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {
            'id': 'testString',
            'instance_id': 'testString',
            'instance_location': 'testString',
            'attachment_id': 'testString',
            'profile_name': 'testString',
        }
        # Construct a dict representation of a InputVariable model
        input_variable_model = {
            'account_id': '$configs[].name[\"account-stage\"].inputs.account_id',
            'resource_group': 'stage',
            'access_tags': '["env:stage"]',
            'logdna_name': 'Name of the LogDNA stage service instance',
            'sysdig_name': 'Name of the SysDig stage service instance',
        }
        # Construct a dict representation of a ProjectConfigSetting model
        project_config_setting_model = {
            'IBMCLOUD_TOOLCHAIN_ENDPOINT': 'https://api.us-south.devops.dev.cloud.ibm.com',
        }
        # Construct a dict representation of a ProjectConfigPrototypeDefinitionBlock model
        project_config_prototype_definition_block_model = {
            'name': 'env-stage',
            'description': 'Stage environment configuration, which includes services common to all the environment regions. There must be a blueprint configuring all the services common to the stage regions. It is a terraform_template type of configuration that points to a Github repo hosting the terraform modules that can be deployed by a Schematics Workspace.',
            'labels': ['env:stage', 'governance:test', 'build:0'],
            'environment': 'testString',
            'authorizations': project_config_auth_model,
            'compliance_profile': project_compliance_profile_model,
            'locator_id': '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global',
            'inputs': input_variable_model,
            'settings': project_config_setting_model,
        }
        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {
            'workspace_crn': 'testString',
        }

        response = self.project_service.create_config(
            project_id=project_id_link,
            definition=project_config_prototype_definition_block_model,
            schematics=schematics_workspace_model,
        )

        assert response.get_status_code() == 201
        project_config = response.get_result()
        assert project_config is not None

        config_id_link = project_config['id']

    @needscredentials
    def test_list_projects(self):
        response = self.project_service.list_projects(
            start='testString',
            limit=10,
        )

        assert response.get_status_code() == 200
        project_collection = response.get_result()
        assert project_collection is not None

    @needscredentials
    def test_list_projects_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ProjectsPager(
            client=self.project_service,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ProjectsPager(
            client=self.project_service,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_projects() returned a total of {len(all_results)} items(s) using ProjectsPager.')

    @needscredentials
    def test_get_project(self):
        response = self.project_service.get_project(
            id=project_id_link,
        )

        assert response.get_status_code() == 200
        project = response.get_result()
        assert project is not None

    @needscredentials
    def test_update_project(self):
        # Construct a dict representation of a ProjectPrototypePatchDefinitionBlock model
        project_prototype_patch_definition_block_model = {
            'name': 'acme-microservice',
            'description': 'A microservice to deploy on top of ACME infrastructure.',
            'destroy_on_delete': True,
        }

        response = self.project_service.update_project(
            id=project_id_link,
            definition=project_prototype_patch_definition_block_model,
        )

        assert response.get_status_code() == 200
        project = response.get_result()
        assert project is not None

    @needscredentials
    def test_create_project_environment(self):
        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile_id': 'testString',
            'method': 'api_key',
            'api_key': 'TbcdlprpFODhkpns9e0daOWnAwd2tXwSYtPn8rpEd8d9',
        }
        # Construct a dict representation of a InputVariable model
        input_variable_model = {
            'resource_group': 'stage',
            'region': 'us-south',
        }
        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {
            'id': 'some-profile-id',
            'instance_id': 'some-instance-id',
            'instance_location': 'us-south',
            'attachment_id': 'some-attachment-id',
            'profile_name': 'some-profile-name',
        }
        # Construct a dict representation of a EnvironmentDefinitionRequiredProperties model
        environment_definition_required_properties_model = {
            'name': 'development',
            'description': 'The environment \'development\'',
            'authorizations': project_config_auth_model,
            'inputs': input_variable_model,
            'compliance_profile': project_compliance_profile_model,
        }

        response = self.project_service.create_project_environment(
            project_id=project_id_link,
            definition=environment_definition_required_properties_model,
        )

        assert response.get_status_code() == 201
        environment = response.get_result()
        assert environment is not None

    @needscredentials
    def test_list_project_environments(self):
        response = self.project_service.list_project_environments(
            project_id=project_id_link,
        )

        assert response.get_status_code() == 200
        environment_list_response = response.get_result()
        assert environment_list_response is not None

    @needscredentials
    def test_get_project_environment(self):
        response = self.project_service.get_project_environment(
            project_id=project_id_link,
            id=project_id_link,
        )

        assert response.get_status_code() == 200
        environment = response.get_result()
        assert environment is not None

    @needscredentials
    def test_update_project_environment(self):
        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile_id': 'testString',
            'method': 'api_key',
            'api_key': 'TbcdlprpFODhkpns9e0daOWnAwd2tXwSYtPn8rpEd8d9',
        }
        # Construct a dict representation of a InputVariable model
        input_variable_model = {
            'resource_group': 'stage',
            'region': 'us-south',
        }
        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {
            'id': 'some-profile-id',
            'instance_id': 'some-instance-id',
            'instance_location': 'us-south',
            'attachment_id': 'some-attachment-id',
            'profile_name': 'some-profile-name',
        }
        # Construct a dict representation of a EnvironmentDefinitionProperties model
        environment_definition_properties_model = {
            'name': 'development',
            'description': 'The environment \'development\'',
            'authorizations': project_config_auth_model,
            'inputs': input_variable_model,
            'compliance_profile': project_compliance_profile_model,
        }

        response = self.project_service.update_project_environment(
            project_id=project_id_link,
            id=project_id_link,
            definition=environment_definition_properties_model,
        )

        assert response.get_status_code() == 200
        environment = response.get_result()
        assert environment is not None

    @needscredentials
    def test_list_configs(self):
        response = self.project_service.list_configs(
            project_id=project_id_link,
        )

        assert response.get_status_code() == 200
        project_config_collection = response.get_result()
        assert project_config_collection is not None

    @needscredentials
    def test_get_config(self):
        response = self.project_service.get_config(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 200
        project_config = response.get_result()
        assert project_config is not None

    @needscredentials
    def test_update_config(self):
        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile_id': 'testString',
            'method': 'api_key',
            'api_key': 'testString',
        }
        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {
            'id': 'testString',
            'instance_id': 'testString',
            'instance_location': 'testString',
            'attachment_id': 'testString',
            'profile_name': 'testString',
        }
        # Construct a dict representation of a InputVariable model
        input_variable_model = {
            'account_id': '$configs[].name[\"account-stage\"].inputs.account_id',
            'resource_group': 'stage',
            'access_tags': '["env:stage"]',
            'logdna_name': 'Name of the LogDNA stage service instance',
            'sysdig_name': 'Name of the SysDig stage service instance',
        }
        # Construct a dict representation of a ProjectConfigSetting model
        project_config_setting_model = {
            'foo': 'testString',
        }
        # Construct a dict representation of a ProjectConfigPrototypePatchDefinitionBlock model
        project_config_prototype_patch_definition_block_model = {
            'name': 'testString',
            'description': 'testString',
            'labels': ['testString'],
            'environment': 'testString',
            'authorizations': project_config_auth_model,
            'compliance_profile': project_compliance_profile_model,
            'locator_id': 'testString',
            'inputs': input_variable_model,
            'settings': project_config_setting_model,
        }

        response = self.project_service.update_config(
            project_id=project_id_link,
            id=config_id_link,
            definition=project_config_prototype_patch_definition_block_model,
        )

        assert response.get_status_code() == 200
        project_config = response.get_result()
        assert project_config is not None

    @needscredentials
    def test_force_approve(self):
        response = self.project_service.force_approve(
            project_id=project_id_link,
            id=config_id_link,
            comment='Approving the changes',
        )

        assert response.get_status_code() == 201
        project_config_version = response.get_result()
        assert project_config_version is not None

    @needscredentials
    def test_approve(self):
        response = self.project_service.approve(
            project_id=project_id_link,
            id=config_id_link,
            comment='Approving the changes',
        )

        assert response.get_status_code() == 201
        project_config_version = response.get_result()
        assert project_config_version is not None

    @needscredentials
    def test_validate_config(self):
        response = self.project_service.validate_config(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 202
        project_config_version = response.get_result()
        assert project_config_version is not None

    @needscredentials
    def test_deploy_config(self):
        response = self.project_service.deploy_config(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 202
        project_config_version = response.get_result()
        assert project_config_version is not None

    @needscredentials
    def test_undeploy_config(self):
        response = self.project_service.undeploy_config(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_sync_config(self):
        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {
            'workspace_crn': 'crn:v1:staging:public:schematics:us-south:a/38acaf4469814090a4e675dc0c317a0d:95ad49de-ab96-4e7d-a08c-45c38aa448e6:workspace:us-south.workspace.service.e0106139',
        }

        response = self.project_service.sync_config(
            project_id=project_id_link,
            id=config_id_link,
            schematics=schematics_workspace_model,
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_list_config_resources(self):
        response = self.project_service.list_config_resources(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 200
        project_config_resource_collection = response.get_result()
        assert project_config_resource_collection is not None

    @needscredentials
    def test_list_config_versions(self):
        response = self.project_service.list_config_versions(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 200
        project_config_version_summary_collection = response.get_result()
        assert project_config_version_summary_collection is not None

    @needscredentials
    def test_get_config_version(self):
        response = self.project_service.get_config_version(
            project_id=project_id_link,
            id=config_id_link,
            version=38,
        )

        assert response.get_status_code() == 200
        project_config_version = response.get_result()
        assert project_config_version is not None

    @needscredentials
    def test_delete_project_environment(self):
        response = self.project_service.delete_project_environment(
            project_id=project_id_link,
            id=project_id_link,
        )

        assert response.get_status_code() == 200
        environment_delete_response = response.get_result()
        assert environment_delete_response is not None

    @needscredentials
    def test_delete_config(self):
        response = self.project_service.delete_config(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 200
        project_config_delete = response.get_result()
        assert project_config_delete is not None

    @needscredentials
    def test_delete_config_version(self):
        response = self.project_service.delete_config_version(
            project_id=project_id_link,
            id=config_id_link,
            version=38,
        )

        assert response.get_status_code() == 200
        project_config_delete = response.get_result()
        assert project_config_delete is not None

    @needscredentials
    def test_delete_project(self):
        response = self.project_service.delete_project(
            id=project_id_link,
        )

        assert response.get_status_code() == 204
