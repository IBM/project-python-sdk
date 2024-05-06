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
Integration Tests for ProjectV1
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_project_sdk.project_v1 import *

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

            cls.project_service = ProjectV1.new_instance()
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
            'destroy_on_delete': True,
            'description': 'A microservice to deploy on top of ACME infrastructure.',
            'monitoring_enabled': False,
        }
        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {
            'id': 'testString',
            'instance_id': 'testString',
            'instance_location': 'testString',
            'attachment_id': 'testString',
            'profile_name': 'testString',
        }
        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile_id': 'testString',
            'method': 'api_key',
            'api_key': 'testString',
        }
        # Construct a dict representation of a ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype model
        project_config_definition_prototype_model = {
            'compliance_profile': project_compliance_profile_model,
            'locator_id': '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global',
            'description': 'The stage account configuration.',
            'name': 'account-stage',
            'environment_id': 'testString',
            'authorizations': project_config_auth_model,
            'inputs': {'anyKey': 'anyValue'},
            'settings': {'anyKey': 'anyValue'},
        }
        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {
            'workspace_crn': 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::',
        }
        # Construct a dict representation of a ProjectConfigPrototype model
        project_config_prototype_model = {
            'definition': project_config_definition_prototype_model,
            'schematics': schematics_workspace_model,
        }
        # Construct a dict representation of a EnvironmentDefinitionRequiredProperties model
        environment_definition_required_properties_model = {
            'description': 'testString',
            'name': 'testString',
            'authorizations': project_config_auth_model,
            'inputs': {'anyKey': 'anyValue'},
            'compliance_profile': project_compliance_profile_model,
        }
        # Construct a dict representation of a EnvironmentPrototype model
        environment_prototype_model = {
            'definition': environment_definition_required_properties_model,
        }

        response = self.project_service.create_project(
            definition=project_prototype_definition_model,
            location='us-south',
            resource_group='Default',
            configs=[project_config_prototype_model],
            environments=[environment_prototype_model],
        )

        assert response.get_status_code() == 201
        project = response.get_result()
        assert project is not None

        project_id_link = project['id']

    @needscredentials
    def test_create_config(self):
        global config_id_link

        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {
            'id': 'testString',
            'instance_id': 'testString',
            'instance_location': 'testString',
            'attachment_id': 'testString',
            'profile_name': 'testString',
        }
        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile_id': 'testString',
            'method': 'api_key',
            'api_key': 'testString',
        }
        # Construct a dict representation of a ProjectConfigDefinitionPrototypeDAConfigDefinitionPropertiesPrototype model
        project_config_definition_prototype_model = {
            'compliance_profile': project_compliance_profile_model,
            'locator_id': '1082e7d2-5e2f-0a11-a3bc-f88a8e1931fc.018edf04-e772-4ca2-9785-03e8e03bef72-global',
            'description': 'The stage environment configuration.',
            'name': 'env-stage',
            'environment_id': 'testString',
            'authorizations': project_config_auth_model,
            'inputs': {
                'account_id': 'account_id',
                'resource_group': 'stage',
                'access_tags': ['env:stage'],
                'logdna_name': 'LogDNA_stage_service',
                'sysdig_name': 'SysDig_stage_service',
            },
            'settings': {'anyKey': 'anyValue'},
        }
        # Construct a dict representation of a SchematicsWorkspace model
        schematics_workspace_model = {
            'workspace_crn': 'crn:v1:staging:public:project:us-south:a/4e1c48fcf8ac33c0a2441e4139f189ae:bf40ad13-b107-446a-8286-c6d576183bb1::',
        }

        response = self.project_service.create_config(
            project_id=project_id_link,
            definition=project_config_definition_prototype_model,
            schematics=schematics_workspace_model,
        )

        assert response.get_status_code() == 201
        project_config = response.get_result()
        assert project_config is not None

        config_id_link = project_config['id']

    @needscredentials
    def test_list_projects(self):
        response = self.project_service.list_projects(
            token='testString',
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
        # Construct a dict representation of a ProjectPatchDefinitionBlock model
        project_patch_definition_block_model = {
            'name': 'acme-microservice',
            'destroy_on_delete': True,
            'description': 'A microservice to deploy on top of ACME infrastructure.',
            'monitoring_enabled': True,
        }

        response = self.project_service.update_project(
            id=project_id_link,
            definition=project_patch_definition_block_model,
        )

        assert response.get_status_code() == 200
        project = response.get_result()
        assert project is not None

    @needscredentials
    def test_create_project_environment(self):
        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile_id': 'Profile-9ac10c5c-195c-41ef-b465-68a6b6dg5f12',
            'method': 'trusted_profile',
            'api_key': 'testString',
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
            'description': 'The environment development.',
            'name': 'development',
            'authorizations': project_config_auth_model,
            'inputs': {'resource_group': 'stage', 'region': 'us-south'},
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
            token='testString',
            limit=10,
        )

        assert response.get_status_code() == 200
        environment_collection = response.get_result()
        assert environment_collection is not None

    @needscredentials
    def test_list_project_environments_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ProjectEnvironmentsPager(
            client=self.project_service,
            project_id=project_id_link,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ProjectEnvironmentsPager(
            client=self.project_service,
            project_id=project_id_link,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(
            f'\nlist_project_environments() returned a total of {len(all_results)} items(s) using ProjectEnvironmentsPager.'
        )

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
            'trusted_profile_id': 'Profile-9ac10c5c-195c-41ef-b465-68a6b6dg5f12',
            'method': 'trusted_profile',
            'api_key': 'testString',
        }
        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {
            'id': 'some-profile-id',
            'instance_id': 'some-instance-id',
            'instance_location': 'us-south',
            'attachment_id': 'some-attachment-id',
            'profile_name': 'some-profile-name',
        }
        # Construct a dict representation of a EnvironmentDefinitionPropertiesPatch model
        environment_definition_properties_patch_model = {
            'description': 'The environment development.',
            'name': 'development',
            'authorizations': project_config_auth_model,
            'inputs': {'resource_group': 'stage', 'region': 'us-south'},
            'compliance_profile': project_compliance_profile_model,
        }

        response = self.project_service.update_project_environment(
            project_id=project_id_link,
            id=project_id_link,
            definition=environment_definition_properties_patch_model,
        )

        assert response.get_status_code() == 200
        environment = response.get_result()
        assert environment is not None

    @needscredentials
    def test_list_configs(self):
        response = self.project_service.list_configs(
            project_id=project_id_link,
            token='testString',
            limit=10,
        )

        assert response.get_status_code() == 200
        project_config_collection = response.get_result()
        assert project_config_collection is not None

    @needscredentials
    def test_list_configs_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ConfigsPager(
            client=self.project_service,
            project_id=project_id_link,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ConfigsPager(
            client=self.project_service,
            project_id=project_id_link,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_configs() returned a total of {len(all_results)} items(s) using ConfigsPager.')

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
        # Construct a dict representation of a ProjectComplianceProfile model
        project_compliance_profile_model = {
            'id': 'testString',
            'instance_id': 'testString',
            'instance_location': 'testString',
            'attachment_id': 'testString',
            'profile_name': 'testString',
        }
        # Construct a dict representation of a ProjectConfigAuth model
        project_config_auth_model = {
            'trusted_profile_id': 'testString',
            'method': 'api_key',
            'api_key': 'testString',
        }
        # Construct a dict representation of a ProjectConfigDefinitionPatchDAConfigDefinitionPropertiesPatch model
        project_config_definition_patch_model = {
            'compliance_profile': project_compliance_profile_model,
            'locator_id': 'testString',
            'description': 'testString',
            'name': 'env-stage',
            'environment_id': 'testString',
            'authorizations': project_config_auth_model,
            'inputs': {
                'account_id': 'account_id',
                'resource_group': 'stage',
                'access_tags': ['env:stage'],
                'logdna_name': 'LogDNA_stage_service',
                'sysdig_name': 'SysDig_stage_service',
            },
            'settings': {'anyKey': 'anyValue'},
        }

        response = self.project_service.update_config(
            project_id=project_id_link,
            id=config_id_link,
            definition=project_config_definition_patch_model,
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

        assert response.get_status_code() == 200
        project_config_version = response.get_result()
        assert project_config_version is not None

    @needscredentials
    def test_approve(self):
        response = self.project_service.approve(
            project_id=project_id_link,
            id=config_id_link,
            comment='Approving the changes',
        )

        assert response.get_status_code() == 200
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

        assert response.get_status_code() == 202
        project_config_version = response.get_result()
        assert project_config_version is not None

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
    def test_create_stack_definition(self):
        # Construct a dict representation of a StackDefinitionInputVariable model
        stack_definition_input_variable_model = {
            'name': 'region',
            'type': 'string',
            'description': 'testString',
            'default': 'us-south',
            'required': True,
            'hidden': False,
        }
        # Construct a dict representation of a StackDefinitionOutputVariable model
        stack_definition_output_variable_model = {
            'name': 'vpc_cluster_id',
            'value': 'cluster_id',
        }
        # Construct a dict representation of a StackDefinitionMemberInputPrototype model
        stack_definition_member_input_prototype_model = {
            'name': 'region',
        }
        # Construct a dict representation of a StackDefinitionMemberPrototype model
        stack_definition_member_prototype_model = {
            'name': 'foundation-deployable-architecture',
            'inputs': [stack_definition_member_input_prototype_model],
        }
        # Construct a dict representation of a StackDefinitionBlockPrototype model
        stack_definition_block_prototype_model = {
            'inputs': [stack_definition_input_variable_model],
            'outputs': [stack_definition_output_variable_model],
            'members': [stack_definition_member_prototype_model],
        }

        response = self.project_service.create_stack_definition(
            project_id=project_id_link,
            id=config_id_link,
            stack_definition=stack_definition_block_prototype_model,
        )

        assert response.get_status_code() == 201
        stack_definition = response.get_result()
        assert stack_definition is not None

    @needscredentials
    def test_get_stack_definition(self):
        response = self.project_service.get_stack_definition(
            project_id=project_id_link,
            id=config_id_link,
        )

        assert response.get_status_code() == 200
        stack_definition = response.get_result()
        assert stack_definition is not None

    @needscredentials
    def test_update_stack_definition(self):
        # Construct a dict representation of a StackDefinitionInputVariable model
        stack_definition_input_variable_model = {
            'name': 'region',
            'type': 'string',
            'description': 'testString',
            'default': 'eu-gb',
            'required': True,
            'hidden': False,
        }
        # Construct a dict representation of a StackDefinitionOutputVariable model
        stack_definition_output_variable_model = {
            'name': 'testString',
            'value': 'testString',
        }
        # Construct a dict representation of a StackDefinitionMemberInputPrototype model
        stack_definition_member_input_prototype_model = {
            'name': 'cluster_name',
        }
        # Construct a dict representation of a StackDefinitionMemberPrototype model
        stack_definition_member_prototype_model = {
            'name': 'foundation-deployable-architecture',
            'inputs': [stack_definition_member_input_prototype_model],
        }
        # Construct a dict representation of a StackDefinitionBlockPrototype model
        stack_definition_block_prototype_model = {
            'inputs': [stack_definition_input_variable_model],
            'outputs': [stack_definition_output_variable_model],
            'members': [stack_definition_member_prototype_model],
        }

        response = self.project_service.update_stack_definition(
            project_id=project_id_link,
            id=config_id_link,
            stack_definition=stack_definition_block_prototype_model,
        )

        assert response.get_status_code() == 200
        stack_definition = response.get_result()
        assert stack_definition is not None

    @needscredentials
    def test_export_stack_definition(self):
        # Construct a dict representation of a StackDefinitionExportRequestStackDefinitionExportCatalogRequest model
        stack_definition_export_request_model = {
            'catalog_id': '01e1a9ad-534b-4ab9-996a-b8f2a8653d5c',
            'target_version': 'testString',
            'variation': 'testString',
            'label': 'Stack Deployable Architecture',
            'tags': ['testString'],
        }

        response = self.project_service.export_stack_definition(
            project_id=project_id_link,
            id=config_id_link,
            settings=stack_definition_export_request_model,
        )

        assert response.get_status_code() == 200
        stack_definition_export_response = response.get_result()
        assert stack_definition_export_response is not None

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

        assert response.get_status_code() == 202
        project_delete_response = response.get_result()
        assert project_delete_response is not None
