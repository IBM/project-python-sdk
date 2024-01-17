# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.80.0-29334a73-20230925-151553

"""
Manage infrastructure as code in IBM Cloud.

API Version: 1.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse, get_query_param
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class ProjectV1(BaseService):
    """The project V1 service."""

    DEFAULT_SERVICE_URL = 'https://projects.api.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'project'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'ProjectV1':
        """
        Return a new client for the project service using the specified parameters
               and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(authenticator)
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the project service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Projects
    #########################

    def create_project(
        self,
        definition: 'ProjectPrototypeDefinition',
        location: str,
        resource_group: str,
        *,
        configs: List['ProjectConfigPrototype'] = None,
        environments: List['EnvironmentPrototype'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a project.

        Create a new project and asynchronously setup the tools to manage it. Add a
        deployable architecture by customizing the configuration. After the changes are
        validated and approved, deploy the resources that the project configures.

        :param ProjectPrototypeDefinition definition: The definition of the
               project.
        :param str location: The IBM Cloud location where a resource is deployed.
        :param str resource_group: The resource group name where the project's data
               and tools are created.
        :param List[ProjectConfigPrototype] configs: (optional) The project
               configurations. These configurations are only included in the response of
               creating a project if a configs array is specified in the request payload.
        :param List[EnvironmentPrototype] environments: (optional) The project
               environments. These environments are only included in the response of
               creating a project if a environments array is specified in the request
               payload.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Project` object
        """

        if definition is None:
            raise ValueError('definition must be provided')
        if location is None:
            raise ValueError('location must be provided')
        if resource_group is None:
            raise ValueError('resource_group must be provided')
        definition = convert_model(definition)
        if configs is not None:
            configs = [convert_model(x) for x in configs]
        if environments is not None:
            environments = [convert_model(x) for x in environments]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_project',
        )
        headers.update(sdk_headers)

        data = {
            'definition': definition,
            'location': location,
            'resource_group': resource_group,
            'configs': configs,
            'environments': environments,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/projects'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_projects(
        self,
        *,
        start: str = None,
        limit: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List projects.

        List existing projects. Projects are sorted by ID.

        :param str start: (optional) Marks the last entry that is returned on the
               page. The server uses this parameter to determine the first entry that is
               returned on the next page. If this parameter is not specified, the logical
               first page is returned.
        :param int limit: (optional) Determine the maximum number of resources to
               return. The number of resources that are returned is the same, with the
               exception of the last page.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectCollection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_projects',
        )
        headers.update(sdk_headers)

        params = {
            'start': start,
            'limit': limit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/projects'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_project(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a project.

        Get information about a project.

        :param str id: The unique project ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Project` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_project',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_project(
        self,
        id: str,
        definition: 'ProjectPatchDefinitionBlock',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a project.

        Update a project by the ID.

        :param str id: The unique project ID.
        :param ProjectPatchDefinitionBlock definition: The definition of the
               project.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Project` object
        """

        if not id:
            raise ValueError('id must be provided')
        if definition is None:
            raise ValueError('definition must be provided')
        definition = convert_model(definition)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_project',
        )
        headers.update(sdk_headers)

        data = {
            'definition': definition,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_project(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a project.

        Delete a project document by the ID. A project can only be deleted after deleting
        all of its resources.

        :param str id: The unique project ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_project',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Environments
    #########################

    def create_project_environment(
        self,
        project_id: str,
        definition: 'EnvironmentDefinitionRequiredProperties',
        **kwargs,
    ) -> DetailedResponse:
        """
        Create an environment.

        Create an environment.

        :param str project_id: The unique project ID.
        :param EnvironmentDefinitionRequiredProperties definition: The environment
               definition.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Environment` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if definition is None:
            raise ValueError('definition must be provided')
        definition = convert_model(definition)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_project_environment',
        )
        headers.update(sdk_headers)

        data = {
            'definition': definition,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/environments'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_project_environments(
        self,
        project_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List environments.

        Returns all environments.

        :param str project_id: The unique project ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EnvironmentCollection` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_project_environments',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/environments'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_project_environment(
        self,
        project_id: str,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get an environment.

        Returns an environment.

        :param str project_id: The unique project ID.
        :param str id: The environment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Environment` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_project_environment',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/environments/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_project_environment(
        self,
        project_id: str,
        id: str,
        definition: 'EnvironmentDefinitionProperties',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update an environment.

        Update an environment by the ID.

        :param str project_id: The unique project ID.
        :param str id: The environment ID.
        :param EnvironmentDefinitionProperties definition: The environment
               definition used for updates.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Environment` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        if definition is None:
            raise ValueError('definition must be provided')
        definition = convert_model(definition)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_project_environment',
        )
        headers.update(sdk_headers)

        data = {
            'definition': definition,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/environments/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_project_environment(
        self,
        project_id: str,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an environment.

        Delete an environment in a project by ID.

        :param str project_id: The unique project ID.
        :param str id: The environment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EnvironmentDeleteResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_project_environment',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/environments/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Configurations
    #########################

    def create_config(
        self,
        project_id: str,
        definition: 'ProjectConfigPrototypeDefinitionBlock',
        *,
        schematics: 'SchematicsWorkspace' = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Add a new configuration.

        Add a new configuration to a project.

        :param str project_id: The unique project ID.
        :param ProjectConfigPrototypeDefinitionBlock definition:
        :param SchematicsWorkspace schematics: (optional) A Schematics workspace to
               use for deploying this configuration.
               Either schematics.workspace_crn, definition.locator_id, or both must be
               specified.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfig` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if definition is None:
            raise ValueError('definition must be provided')
        definition = convert_model(definition)
        if schematics is not None:
            schematics = convert_model(schematics)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_config',
        )
        headers.update(sdk_headers)

        data = {
            'definition': definition,
            'schematics': schematics,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_configs(
        self,
        project_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List all project configurations.

        The collection of configurations that are returned.

        :param str project_id: The unique project ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigCollection` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_configs',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id']
        path_param_values = self.encode_path_vars(project_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_config(
        self,
        project_id: str,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a project configuration.

        Returns the specified project configuration in a specific project.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfig` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_config',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_config(
        self,
        project_id: str,
        id: str,
        definition: 'ProjectConfigPatchDefinitionBlock',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a configuration.

        Update a configuration in a project by the ID.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param ProjectConfigPatchDefinitionBlock definition:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfig` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        if definition is None:
            raise ValueError('definition must be provided')
        definition = convert_model(definition)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_config',
        )
        headers.update(sdk_headers)

        data = {
            'definition': definition,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_config(
        self,
        project_id: str,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a configuration in a project by ID.

        Delete a configuration in a project.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigDelete` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_config',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def force_approve(
        self,
        project_id: str,
        id: str,
        comment: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Force approve project configuration.

        Force approve configuration edits to the main configuration with an approving
        comment.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param str comment: Notes on the project draft action. If this is a forced
               approve on the draft configuration, a non-empty comment is required.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigVersion` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        if comment is None:
            raise ValueError('comment must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='force_approve',
        )
        headers.update(sdk_headers)

        data = {
            'comment': comment,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/force_approve'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def approve(
        self,
        project_id: str,
        id: str,
        *,
        comment: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Approve and merge a configuration draft.

        Approve and merge configuration edits to the main configuration.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param str comment: (optional) Notes on the project draft action. If this
               is a forced approve on the draft configuration, a non-empty comment is
               required.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigVersion` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='approve',
        )
        headers.update(sdk_headers)

        data = {
            'comment': comment,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/approve'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def validate_config(
        self,
        project_id: str,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Run a validation check.

        Run a validation check on a given configuration in project. The check includes
        creating or updating the associated schematics workspace with a plan job, running
        the CRA scans, and cost estimatation.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigVersion` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='validate_config',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/validate'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def deploy_config(
        self,
        project_id: str,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Deploy a configuration.

        Deploy a project's configuration. It's an asynchronous operation that can be
        tracked using the get project configuration API with full metadata.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigVersion` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='deploy_config',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/deploy'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def undeploy_config(
        self,
        project_id: str,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Undeploy configuration resources.

        Undeploy a project's configuration resources. The operation undeploys all the
        resources that are deployed with the specific configuration. You can track it by
        using the get project configuration API with full metadata.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='undeploy_config',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/undeploy'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def sync_config(
        self,
        project_id: str,
        id: str,
        *,
        schematics: 'SchematicsWorkspace' = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Sync a project configuration.

        Sync a project configuration by analyzing the associated pipeline runs and
        schematics workspace logs to get the configuration back to a working state.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param SchematicsWorkspace schematics: (optional) A Schematics workspace to
               use for deploying this configuration.
               Either schematics.workspace_crn, definition.locator_id, or both must be
               specified.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        if schematics is not None:
            schematics = convert_model(schematics)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='sync_config',
        )
        headers.update(sdk_headers)

        data = {
            'schematics': schematics,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/sync'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_config_resources(
        self,
        project_id: str,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List the resources deployed by a configuration.

        A list of resources deployed by a configuraton.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigResourceCollection` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_config_resources',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/resources'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_config_versions(
        self,
        project_id: str,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a list of versions of a project configuration.

        Returns a list of previous and current versions of a project configuration in a
        specific project.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigVersionSummaryCollection` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_config_versions',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/versions'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_config_version(
        self,
        project_id: str,
        id: str,
        version: int,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a specific version of a project configuration.

        Returns a specific version of a project configuration in a specific project.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param int version: The configuration version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigVersion` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        if version is None:
            raise ValueError('version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_config_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id', 'version']
        path_param_values = self.encode_path_vars(project_id, id, str(version))
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/versions/{version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_config_version(
        self,
        project_id: str,
        id: str,
        version: int,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a configuration for the specified project ID and version.

        Delete a configuration in a project.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param int version: The configuration version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigDelete` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        if version is None:
            raise ValueError('version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_config_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id', 'version']
        path_param_values = self.encode_path_vars(project_id, id, str(version))
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/versions/{version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class ActionJobApplyMessagesSummary:
    """
    The messages of apply jobs on the configuration.

    :attr List[TerraformLogAnalyzerErrorMessage] error_messages: (optional) The
          collection of error messages.
    :attr List[TerraformLogAnalyzerSuccessMessage] sucess_message: (optional) The
          collection of success messages.
    """

    def __init__(
        self,
        *,
        error_messages: List['TerraformLogAnalyzerErrorMessage'] = None,
        sucess_message: List['TerraformLogAnalyzerSuccessMessage'] = None,
    ) -> None:
        """
        Initialize a ActionJobApplyMessagesSummary object.

        :param List[TerraformLogAnalyzerErrorMessage] error_messages: (optional)
               The collection of error messages.
        :param List[TerraformLogAnalyzerSuccessMessage] sucess_message: (optional)
               The collection of success messages.
        """
        self.error_messages = error_messages
        self.sucess_message = sucess_message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionJobApplyMessagesSummary':
        """Initialize a ActionJobApplyMessagesSummary object from a json dictionary."""
        args = {}
        if 'error_messages' in _dict:
            args['error_messages'] = [
                TerraformLogAnalyzerErrorMessage.from_dict(v) for v in _dict.get('error_messages')
            ]
        if 'sucess_message' in _dict:
            args['sucess_message'] = [
                TerraformLogAnalyzerSuccessMessage.from_dict(v) for v in _dict.get('sucess_message')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionJobApplyMessagesSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'error_messages') and self.error_messages is not None:
            error_messages_list = []
            for v in self.error_messages:
                if isinstance(v, dict):
                    error_messages_list.append(v)
                else:
                    error_messages_list.append(v.to_dict())
            _dict['error_messages'] = error_messages_list
        if hasattr(self, 'sucess_message') and self.sucess_message is not None:
            sucess_message_list = []
            for v in self.sucess_message:
                if isinstance(v, dict):
                    sucess_message_list.append(v)
                else:
                    sucess_message_list.append(v.to_dict())
            _dict['sucess_message'] = sucess_message_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionJobApplyMessagesSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionJobApplyMessagesSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionJobApplyMessagesSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ActionJobApplySummary:
    """
    The summary of the apply jobs on the configuration.

    :attr int success: (optional) The number of applied resources.
    :attr int failed: (optional) The number of failed resources.
    :attr List[str] success_resources: (optional) The collection of successfully
          applied resources.
    :attr List[str] failed_resources: (optional) The collection of failed applied
          resources.
    """

    def __init__(
        self,
        *,
        success: int = None,
        failed: int = None,
        success_resources: List[str] = None,
        failed_resources: List[str] = None,
    ) -> None:
        """
        Initialize a ActionJobApplySummary object.

        :param int success: (optional) The number of applied resources.
        :param int failed: (optional) The number of failed resources.
        :param List[str] success_resources: (optional) The collection of
               successfully applied resources.
        :param List[str] failed_resources: (optional) The collection of failed
               applied resources.
        """
        self.success = success
        self.failed = failed
        self.success_resources = success_resources
        self.failed_resources = failed_resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionJobApplySummary':
        """Initialize a ActionJobApplySummary object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        if 'success_resources' in _dict:
            args['success_resources'] = _dict.get('success_resources')
        if 'failed_resources' in _dict:
            args['failed_resources'] = _dict.get('failed_resources')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionJobApplySummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        if hasattr(self, 'success_resources') and self.success_resources is not None:
            _dict['success_resources'] = self.success_resources
        if hasattr(self, 'failed_resources') and self.failed_resources is not None:
            _dict['failed_resources'] = self.failed_resources
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionJobApplySummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionJobApplySummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionJobApplySummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ActionJobDestroyMessagesSummary:
    """
    The messages of destroy jobs on the configuration.

    :attr List[TerraformLogAnalyzerErrorMessage] error_messages: (optional) The
          collection of error messages.
    """

    def __init__(
        self,
        *,
        error_messages: List['TerraformLogAnalyzerErrorMessage'] = None,
    ) -> None:
        """
        Initialize a ActionJobDestroyMessagesSummary object.

        :param List[TerraformLogAnalyzerErrorMessage] error_messages: (optional)
               The collection of error messages.
        """
        self.error_messages = error_messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionJobDestroyMessagesSummary':
        """Initialize a ActionJobDestroyMessagesSummary object from a json dictionary."""
        args = {}
        if 'error_messages' in _dict:
            args['error_messages'] = [
                TerraformLogAnalyzerErrorMessage.from_dict(v) for v in _dict.get('error_messages')
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionJobDestroyMessagesSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'error_messages') and self.error_messages is not None:
            error_messages_list = []
            for v in self.error_messages:
                if isinstance(v, dict):
                    error_messages_list.append(v)
                else:
                    error_messages_list.append(v.to_dict())
            _dict['error_messages'] = error_messages_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionJobDestroyMessagesSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionJobDestroyMessagesSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionJobDestroyMessagesSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ActionJobDestroySummary:
    """
    The summary of the destroy jobs on the configuration.

    :attr int success: (optional) The number of destroyed resources.
    :attr int failed: (optional) The number of failed resources.
    :attr int tainted: (optional) The number of tainted resources.
    :attr ActionJobDestroySummaryResources resources: (optional) The destroy
          resources results from the job.
    """

    def __init__(
        self,
        *,
        success: int = None,
        failed: int = None,
        tainted: int = None,
        resources: 'ActionJobDestroySummaryResources' = None,
    ) -> None:
        """
        Initialize a ActionJobDestroySummary object.

        :param int success: (optional) The number of destroyed resources.
        :param int failed: (optional) The number of failed resources.
        :param int tainted: (optional) The number of tainted resources.
        :param ActionJobDestroySummaryResources resources: (optional) The destroy
               resources results from the job.
        """
        self.success = success
        self.failed = failed
        self.tainted = tainted
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionJobDestroySummary':
        """Initialize a ActionJobDestroySummary object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        if 'tainted' in _dict:
            args['tainted'] = _dict.get('tainted')
        if 'resources' in _dict:
            args['resources'] = ActionJobDestroySummaryResources.from_dict(_dict.get('resources'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionJobDestroySummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        if hasattr(self, 'tainted') and self.tainted is not None:
            _dict['tainted'] = self.tainted
        if hasattr(self, 'resources') and self.resources is not None:
            if isinstance(self.resources, dict):
                _dict['resources'] = self.resources
            else:
                _dict['resources'] = self.resources.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionJobDestroySummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionJobDestroySummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionJobDestroySummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ActionJobDestroySummaryResources:
    """
    The destroy resources results from the job.

    :attr List[str] success: (optional) The collection of destroyed resources.
    :attr List[str] failed: (optional) The collection of failed resources.
    :attr List[str] tainted: (optional) The collection of tainted resources.
    """

    def __init__(
        self,
        *,
        success: List[str] = None,
        failed: List[str] = None,
        tainted: List[str] = None,
    ) -> None:
        """
        Initialize a ActionJobDestroySummaryResources object.

        :param List[str] success: (optional) The collection of destroyed resources.
        :param List[str] failed: (optional) The collection of failed resources.
        :param List[str] tainted: (optional) The collection of tainted resources.
        """
        self.success = success
        self.failed = failed
        self.tainted = tainted

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionJobDestroySummaryResources':
        """Initialize a ActionJobDestroySummaryResources object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        if 'tainted' in _dict:
            args['tainted'] = _dict.get('tainted')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionJobDestroySummaryResources object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        if hasattr(self, 'tainted') and self.tainted is not None:
            _dict['tainted'] = self.tainted
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionJobDestroySummaryResources object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionJobDestroySummaryResources') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionJobDestroySummaryResources') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ActionJobMessageSummary:
    """
    The message summaries of jobs on the configuration.

    :attr int info: (optional) The number of info messages.
    :attr int debug: (optional) The number of debug messages.
    :attr int error: (optional) The number of error messages.
    """

    def __init__(
        self,
        *,
        info: int = None,
        debug: int = None,
        error: int = None,
    ) -> None:
        """
        Initialize a ActionJobMessageSummary object.

        :param int info: (optional) The number of info messages.
        :param int debug: (optional) The number of debug messages.
        :param int error: (optional) The number of error messages.
        """
        self.info = info
        self.debug = debug
        self.error = error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionJobMessageSummary':
        """Initialize a ActionJobMessageSummary object from a json dictionary."""
        args = {}
        if 'info' in _dict:
            args['info'] = _dict.get('info')
        if 'debug' in _dict:
            args['debug'] = _dict.get('debug')
        if 'error' in _dict:
            args['error'] = _dict.get('error')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionJobMessageSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'info') and self.info is not None:
            _dict['info'] = self.info
        if hasattr(self, 'debug') and self.debug is not None:
            _dict['debug'] = self.debug
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionJobMessageSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionJobMessageSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionJobMessageSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ActionJobPlanMessagesSummary:
    """
    The plan messages on the configuration.

    :attr List[TerraformLogAnalyzerErrorMessage] error_messages: (optional) The
          collection of error messages.
    :attr List[str] sucess_message: (optional) The collection of success messages.
    :attr List[str] update_message: (optional) The collection of update messages.
    :attr List[str] destroy_message: (optional) The collection of destroy messages.
    """

    def __init__(
        self,
        *,
        error_messages: List['TerraformLogAnalyzerErrorMessage'] = None,
        sucess_message: List[str] = None,
        update_message: List[str] = None,
        destroy_message: List[str] = None,
    ) -> None:
        """
        Initialize a ActionJobPlanMessagesSummary object.

        :param List[TerraformLogAnalyzerErrorMessage] error_messages: (optional)
               The collection of error messages.
        :param List[str] sucess_message: (optional) The collection of success
               messages.
        :param List[str] update_message: (optional) The collection of update
               messages.
        :param List[str] destroy_message: (optional) The collection of destroy
               messages.
        """
        self.error_messages = error_messages
        self.sucess_message = sucess_message
        self.update_message = update_message
        self.destroy_message = destroy_message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionJobPlanMessagesSummary':
        """Initialize a ActionJobPlanMessagesSummary object from a json dictionary."""
        args = {}
        if 'error_messages' in _dict:
            args['error_messages'] = [
                TerraformLogAnalyzerErrorMessage.from_dict(v) for v in _dict.get('error_messages')
            ]
        if 'sucess_message' in _dict:
            args['sucess_message'] = _dict.get('sucess_message')
        if 'update_message' in _dict:
            args['update_message'] = _dict.get('update_message')
        if 'destroy_message' in _dict:
            args['destroy_message'] = _dict.get('destroy_message')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionJobPlanMessagesSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'error_messages') and self.error_messages is not None:
            error_messages_list = []
            for v in self.error_messages:
                if isinstance(v, dict):
                    error_messages_list.append(v)
                else:
                    error_messages_list.append(v.to_dict())
            _dict['error_messages'] = error_messages_list
        if hasattr(self, 'sucess_message') and self.sucess_message is not None:
            _dict['sucess_message'] = self.sucess_message
        if hasattr(self, 'update_message') and self.update_message is not None:
            _dict['update_message'] = self.update_message
        if hasattr(self, 'destroy_message') and self.destroy_message is not None:
            _dict['destroy_message'] = self.destroy_message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionJobPlanMessagesSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionJobPlanMessagesSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionJobPlanMessagesSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ActionJobPlanSummary:
    """
    The summary of the plan jobs on the configuration.

    :attr int add: (optional) The number of resources to be added.
    :attr int failed: (optional) The number of resources that failed during the plan
          job.
    :attr int update: (optional) The number of resources to be updated.
    :attr int destroy: (optional) The number of resources to be destroyed.
    :attr List[str] add_resources: (optional) The collection of planned added
          resources.
    :attr List[str] failed_resources: (optional) The collection of failed planned
          resources.
    :attr List[str] updated_resources: (optional) The collection of planned updated
          resources.
    :attr List[str] destroy_resources: (optional) The collection of planned destroy
          resources.
    """

    def __init__(
        self,
        *,
        add: int = None,
        failed: int = None,
        update: int = None,
        destroy: int = None,
        add_resources: List[str] = None,
        failed_resources: List[str] = None,
        updated_resources: List[str] = None,
        destroy_resources: List[str] = None,
    ) -> None:
        """
        Initialize a ActionJobPlanSummary object.

        :param int add: (optional) The number of resources to be added.
        :param int failed: (optional) The number of resources that failed during
               the plan job.
        :param int update: (optional) The number of resources to be updated.
        :param int destroy: (optional) The number of resources to be destroyed.
        :param List[str] add_resources: (optional) The collection of planned added
               resources.
        :param List[str] failed_resources: (optional) The collection of failed
               planned resources.
        :param List[str] updated_resources: (optional) The collection of planned
               updated resources.
        :param List[str] destroy_resources: (optional) The collection of planned
               destroy resources.
        """
        self.add = add
        self.failed = failed
        self.update = update
        self.destroy = destroy
        self.add_resources = add_resources
        self.failed_resources = failed_resources
        self.updated_resources = updated_resources
        self.destroy_resources = destroy_resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionJobPlanSummary':
        """Initialize a ActionJobPlanSummary object from a json dictionary."""
        args = {}
        if 'add' in _dict:
            args['add'] = _dict.get('add')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        if 'update' in _dict:
            args['update'] = _dict.get('update')
        if 'destroy' in _dict:
            args['destroy'] = _dict.get('destroy')
        if 'add_resources' in _dict:
            args['add_resources'] = _dict.get('add_resources')
        if 'failed_resources' in _dict:
            args['failed_resources'] = _dict.get('failed_resources')
        if 'updated_resources' in _dict:
            args['updated_resources'] = _dict.get('updated_resources')
        if 'destroy_resources' in _dict:
            args['destroy_resources'] = _dict.get('destroy_resources')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionJobPlanSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'add') and self.add is not None:
            _dict['add'] = self.add
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        if hasattr(self, 'update') and self.update is not None:
            _dict['update'] = self.update
        if hasattr(self, 'destroy') and self.destroy is not None:
            _dict['destroy'] = self.destroy
        if hasattr(self, 'add_resources') and self.add_resources is not None:
            _dict['add_resources'] = self.add_resources
        if hasattr(self, 'failed_resources') and self.failed_resources is not None:
            _dict['failed_resources'] = self.failed_resources
        if hasattr(self, 'updated_resources') and self.updated_resources is not None:
            _dict['updated_resources'] = self.updated_resources
        if hasattr(self, 'destroy_resources') and self.destroy_resources is not None:
            _dict['destroy_resources'] = self.destroy_resources
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionJobPlanSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionJobPlanSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionJobPlanSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ActionJobSummary:
    """
    The summaries of jobs that were performed on the configuration.

    :attr ActionJobPlanSummary plan_summary: The summary of the plan jobs on the
          configuration.
    :attr ActionJobApplySummary apply_summary: The summary of the apply jobs on the
          configuration.
    :attr ActionJobDestroySummary destroy_summary: The summary of the destroy jobs
          on the configuration.
    :attr ActionJobMessageSummary message_summary: The message summaries of jobs on
          the configuration.
    :attr ActionJobPlanMessagesSummary plan_messages: The plan messages on the
          configuration.
    :attr ActionJobApplyMessagesSummary apply_messages: The messages of apply jobs
          on the configuration.
    :attr ActionJobDestroyMessagesSummary destroy_messages: The messages of destroy
          jobs on the configuration.
    """

    def __init__(
        self,
        plan_summary: 'ActionJobPlanSummary',
        apply_summary: 'ActionJobApplySummary',
        destroy_summary: 'ActionJobDestroySummary',
        message_summary: 'ActionJobMessageSummary',
        plan_messages: 'ActionJobPlanMessagesSummary',
        apply_messages: 'ActionJobApplyMessagesSummary',
        destroy_messages: 'ActionJobDestroyMessagesSummary',
    ) -> None:
        """
        Initialize a ActionJobSummary object.

        :param ActionJobPlanSummary plan_summary: The summary of the plan jobs on
               the configuration.
        :param ActionJobApplySummary apply_summary: The summary of the apply jobs
               on the configuration.
        :param ActionJobDestroySummary destroy_summary: The summary of the destroy
               jobs on the configuration.
        :param ActionJobMessageSummary message_summary: The message summaries of
               jobs on the configuration.
        :param ActionJobPlanMessagesSummary plan_messages: The plan messages on the
               configuration.
        :param ActionJobApplyMessagesSummary apply_messages: The messages of apply
               jobs on the configuration.
        :param ActionJobDestroyMessagesSummary destroy_messages: The messages of
               destroy jobs on the configuration.
        """
        self.plan_summary = plan_summary
        self.apply_summary = apply_summary
        self.destroy_summary = destroy_summary
        self.message_summary = message_summary
        self.plan_messages = plan_messages
        self.apply_messages = apply_messages
        self.destroy_messages = destroy_messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionJobSummary':
        """Initialize a ActionJobSummary object from a json dictionary."""
        args = {}
        if 'plan_summary' in _dict:
            args['plan_summary'] = ActionJobPlanSummary.from_dict(_dict.get('plan_summary'))
        else:
            raise ValueError('Required property \'plan_summary\' not present in ActionJobSummary JSON')
        if 'apply_summary' in _dict:
            args['apply_summary'] = ActionJobApplySummary.from_dict(_dict.get('apply_summary'))
        else:
            raise ValueError('Required property \'apply_summary\' not present in ActionJobSummary JSON')
        if 'destroy_summary' in _dict:
            args['destroy_summary'] = ActionJobDestroySummary.from_dict(_dict.get('destroy_summary'))
        else:
            raise ValueError('Required property \'destroy_summary\' not present in ActionJobSummary JSON')
        if 'message_summary' in _dict:
            args['message_summary'] = ActionJobMessageSummary.from_dict(_dict.get('message_summary'))
        else:
            raise ValueError('Required property \'message_summary\' not present in ActionJobSummary JSON')
        if 'plan_messages' in _dict:
            args['plan_messages'] = ActionJobPlanMessagesSummary.from_dict(_dict.get('plan_messages'))
        else:
            raise ValueError('Required property \'plan_messages\' not present in ActionJobSummary JSON')
        if 'apply_messages' in _dict:
            args['apply_messages'] = ActionJobApplyMessagesSummary.from_dict(_dict.get('apply_messages'))
        else:
            raise ValueError('Required property \'apply_messages\' not present in ActionJobSummary JSON')
        if 'destroy_messages' in _dict:
            args['destroy_messages'] = ActionJobDestroyMessagesSummary.from_dict(_dict.get('destroy_messages'))
        else:
            raise ValueError('Required property \'destroy_messages\' not present in ActionJobSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionJobSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'plan_summary') and self.plan_summary is not None:
            if isinstance(self.plan_summary, dict):
                _dict['plan_summary'] = self.plan_summary
            else:
                _dict['plan_summary'] = self.plan_summary.to_dict()
        if hasattr(self, 'apply_summary') and self.apply_summary is not None:
            if isinstance(self.apply_summary, dict):
                _dict['apply_summary'] = self.apply_summary
            else:
                _dict['apply_summary'] = self.apply_summary.to_dict()
        if hasattr(self, 'destroy_summary') and self.destroy_summary is not None:
            if isinstance(self.destroy_summary, dict):
                _dict['destroy_summary'] = self.destroy_summary
            else:
                _dict['destroy_summary'] = self.destroy_summary.to_dict()
        if hasattr(self, 'message_summary') and self.message_summary is not None:
            if isinstance(self.message_summary, dict):
                _dict['message_summary'] = self.message_summary
            else:
                _dict['message_summary'] = self.message_summary.to_dict()
        if hasattr(self, 'plan_messages') and self.plan_messages is not None:
            if isinstance(self.plan_messages, dict):
                _dict['plan_messages'] = self.plan_messages
            else:
                _dict['plan_messages'] = self.plan_messages.to_dict()
        if hasattr(self, 'apply_messages') and self.apply_messages is not None:
            if isinstance(self.apply_messages, dict):
                _dict['apply_messages'] = self.apply_messages
            else:
                _dict['apply_messages'] = self.apply_messages.to_dict()
        if hasattr(self, 'destroy_messages') and self.destroy_messages is not None:
            if isinstance(self.destroy_messages, dict):
                _dict['destroy_messages'] = self.destroy_messages
            else:
                _dict['destroy_messages'] = self.destroy_messages.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionJobSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionJobSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionJobSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ActionJobWithIdAndSummary:
    """
    A brief summary of an action.

    :attr str id: The unique ID.
    :attr ActionJobSummary summary: The summaries of jobs that were performed on the
          configuration.
    """

    def __init__(
        self,
        id: str,
        summary: 'ActionJobSummary',
    ) -> None:
        """
        Initialize a ActionJobWithIdAndSummary object.

        :param str id: The unique ID.
        :param ActionJobSummary summary: The summaries of jobs that were performed
               on the configuration.
        """
        self.id = id
        self.summary = summary

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionJobWithIdAndSummary':
        """Initialize a ActionJobWithIdAndSummary object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ActionJobWithIdAndSummary JSON')
        if 'summary' in _dict:
            args['summary'] = ActionJobSummary.from_dict(_dict.get('summary'))
        else:
            raise ValueError('Required property \'summary\' not present in ActionJobWithIdAndSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionJobWithIdAndSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'summary') and self.summary is not None:
            if isinstance(self.summary, dict):
                _dict['summary'] = self.summary
            else:
                _dict['summary'] = self.summary.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionJobWithIdAndSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionJobWithIdAndSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionJobWithIdAndSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CodeRiskAnalyzerLogsSummary:
    """
    The Code Risk Analyzer logs summary of the configuration.

    :attr str total: (optional) The total number of Code Risk Analyzer rules that
          were applied in the scan.
    :attr str passed: (optional) The number of Code Risk Analyzer rules that passed
          in the scan.
    :attr str failed: (optional) The number of Code Risk Analyzer rules that failed
          in the scan.
    :attr str skipped: (optional) The number of Code Risk Analyzer rules that were
          skipped in the scan.
    """

    def __init__(
        self,
        *,
        total: str = None,
        passed: str = None,
        failed: str = None,
        skipped: str = None,
    ) -> None:
        """
        Initialize a CodeRiskAnalyzerLogsSummary object.

        :param str total: (optional) The total number of Code Risk Analyzer rules
               that were applied in the scan.
        :param str passed: (optional) The number of Code Risk Analyzer rules that
               passed in the scan.
        :param str failed: (optional) The number of Code Risk Analyzer rules that
               failed in the scan.
        :param str skipped: (optional) The number of Code Risk Analyzer rules that
               were skipped in the scan.
        """
        self.total = total
        self.passed = passed
        self.failed = failed
        self.skipped = skipped

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CodeRiskAnalyzerLogsSummary':
        """Initialize a CodeRiskAnalyzerLogsSummary object from a json dictionary."""
        args = {}
        if 'total' in _dict:
            args['total'] = _dict.get('total')
        if 'passed' in _dict:
            args['passed'] = _dict.get('passed')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        if 'skipped' in _dict:
            args['skipped'] = _dict.get('skipped')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CodeRiskAnalyzerLogsSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        if hasattr(self, 'passed') and self.passed is not None:
            _dict['passed'] = self.passed
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        if hasattr(self, 'skipped') and self.skipped is not None:
            _dict['skipped'] = self.skipped
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CodeRiskAnalyzerLogsSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CodeRiskAnalyzerLogsSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CodeRiskAnalyzerLogsSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CumulativeNeedsAttention:
    """
    CumulativeNeedsAttention.

    :attr str event: (optional) The event name.
    :attr str event_id: (optional) A unique ID for that individual event.
    :attr str config_id: (optional) A unique ID for the configuration.
    :attr int config_version: (optional) The version number of the configuration.
    """

    def __init__(
        self,
        *,
        event: str = None,
        event_id: str = None,
        config_id: str = None,
        config_version: int = None,
    ) -> None:
        """
        Initialize a CumulativeNeedsAttention object.

        :param str event: (optional) The event name.
        :param str event_id: (optional) A unique ID for that individual event.
        :param str config_id: (optional) A unique ID for the configuration.
        :param int config_version: (optional) The version number of the
               configuration.
        """
        self.event = event
        self.event_id = event_id
        self.config_id = config_id
        self.config_version = config_version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CumulativeNeedsAttention':
        """Initialize a CumulativeNeedsAttention object from a json dictionary."""
        args = {}
        if 'event' in _dict:
            args['event'] = _dict.get('event')
        if 'event_id' in _dict:
            args['event_id'] = _dict.get('event_id')
        if 'config_id' in _dict:
            args['config_id'] = _dict.get('config_id')
        if 'config_version' in _dict:
            args['config_version'] = _dict.get('config_version')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CumulativeNeedsAttention object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'event') and self.event is not None:
            _dict['event'] = self.event
        if hasattr(self, 'event_id') and self.event_id is not None:
            _dict['event_id'] = self.event_id
        if hasattr(self, 'config_id') and self.config_id is not None:
            _dict['config_id'] = self.config_id
        if hasattr(self, 'config_version') and self.config_version is not None:
            _dict['config_version'] = self.config_version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CumulativeNeedsAttention object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CumulativeNeedsAttention') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CumulativeNeedsAttention') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Environment:
    """
    The definition of a project environment.

    :attr str id: The environment id as a friendly name.
    :attr ProjectReference project: The project referenced by this resource.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr str target_account: (optional) The target account ID derived from the
          authentication block values.
    :attr datetime modified_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr str href: A URL.
    :attr EnvironmentDefinitionRequiredProperties definition: The environment
          definition.
    """

    def __init__(
        self,
        id: str,
        project: 'ProjectReference',
        created_at: datetime,
        modified_at: datetime,
        href: str,
        definition: 'EnvironmentDefinitionRequiredProperties',
        *,
        target_account: str = None,
    ) -> None:
        """
        Initialize a Environment object.

        :param str id: The environment id as a friendly name.
        :param ProjectReference project: The project referenced by this resource.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param datetime modified_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param str href: A URL.
        :param EnvironmentDefinitionRequiredProperties definition: The environment
               definition.
        :param str target_account: (optional) The target account ID derived from
               the authentication block values.
        """
        self.id = id
        self.project = project
        self.created_at = created_at
        self.target_account = target_account
        self.modified_at = modified_at
        self.href = href
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Environment':
        """Initialize a Environment object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Environment JSON')
        if 'project' in _dict:
            args['project'] = ProjectReference.from_dict(_dict.get('project'))
        else:
            raise ValueError('Required property \'project\' not present in Environment JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in Environment JSON')
        if 'target_account' in _dict:
            args['target_account'] = _dict.get('target_account')
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        else:
            raise ValueError('Required property \'modified_at\' not present in Environment JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in Environment JSON')
        if 'definition' in _dict:
            args['definition'] = EnvironmentDefinitionRequiredProperties.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in Environment JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Environment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'project') and self.project is not None:
            if isinstance(self.project, dict):
                _dict['project'] = self.project
            else:
                _dict['project'] = self.project.to_dict()
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'target_account') and self.target_account is not None:
            _dict['target_account'] = self.target_account
        if hasattr(self, 'modified_at') and self.modified_at is not None:
            _dict['modified_at'] = datetime_to_string(self.modified_at)
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Environment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Environment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Environment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnvironmentCollection:
    """
    The list environment response.

    :attr List[Environment] environments: (optional) The environments.
    """

    def __init__(
        self,
        *,
        environments: List['Environment'] = None,
    ) -> None:
        """
        Initialize a EnvironmentCollection object.

        :param List[Environment] environments: (optional) The environments.
        """
        self.environments = environments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentCollection':
        """Initialize a EnvironmentCollection object from a json dictionary."""
        args = {}
        if 'environments' in _dict:
            args['environments'] = [Environment.from_dict(v) for v in _dict.get('environments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environments') and self.environments is not None:
            environments_list = []
            for v in self.environments:
                if isinstance(v, dict):
                    environments_list.append(v)
                else:
                    environments_list.append(v.to_dict())
            _dict['environments'] = environments_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvironmentCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnvironmentDefinitionNameDescription:
    """
    The environment definition used in the project collection.

    :attr str name: (optional) The name of the environment.  It is unique within the
          account across projects and regions.
    :attr str description: (optional) The description of the environment.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
    ) -> None:
        """
        Initialize a EnvironmentDefinitionNameDescription object.

        :param str name: (optional) The name of the environment.  It is unique
               within the account across projects and regions.
        :param str description: (optional) The description of the environment.
        """
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentDefinitionNameDescription':
        """Initialize a EnvironmentDefinitionNameDescription object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentDefinitionNameDescription object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvironmentDefinitionNameDescription object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentDefinitionNameDescription') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentDefinitionNameDescription') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnvironmentDefinitionProperties:
    """
    The environment definition used for updates.

    :attr str name: (optional) The name of the environment.  It is unique within the
          account across projects and regions.
    :attr str description: (optional) The description of the environment.
    :attr ProjectConfigAuth authorizations: (optional) The authorization details.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr dict inputs: (optional) The input variables for configuration definition
          and environment.
    :attr ProjectComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        inputs: dict = None,
        compliance_profile: 'ProjectComplianceProfile' = None,
    ) -> None:
        """
        Initialize a EnvironmentDefinitionProperties object.

        :param str name: (optional) The name of the environment.  It is unique
               within the account across projects and regions.
        :param str description: (optional) The description of the environment.
        :param ProjectConfigAuth authorizations: (optional) The authorization
               details. You can authorize by using a trusted profile or an API key in
               Secrets Manager.
        :param dict inputs: (optional) The input variables for configuration
               definition and environment.
        :param ProjectComplianceProfile compliance_profile: (optional) The profile
               required for compliance.
        """
        self.name = name
        self.description = description
        self.authorizations = authorizations
        self.inputs = inputs
        self.compliance_profile = compliance_profile

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentDefinitionProperties':
        """Initialize a EnvironmentDefinitionProperties object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'inputs' in _dict:
            args['inputs'] = _dict.get('inputs')
        if 'compliance_profile' in _dict:
            args['compliance_profile'] = ProjectComplianceProfile.from_dict(_dict.get('compliance_profile'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentDefinitionProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'authorizations') and self.authorizations is not None:
            if isinstance(self.authorizations, dict):
                _dict['authorizations'] = self.authorizations
            else:
                _dict['authorizations'] = self.authorizations.to_dict()
        if hasattr(self, 'inputs') and self.inputs is not None:
            _dict['inputs'] = self.inputs
        if hasattr(self, 'compliance_profile') and self.compliance_profile is not None:
            if isinstance(self.compliance_profile, dict):
                _dict['compliance_profile'] = self.compliance_profile
            else:
                _dict['compliance_profile'] = self.compliance_profile.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvironmentDefinitionProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentDefinitionProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentDefinitionProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnvironmentDefinitionRequiredProperties:
    """
    The environment definition.

    :attr str name: The name of the environment.  It is unique within the account
          across projects and regions.
    :attr str description: (optional) The description of the environment.
    :attr ProjectConfigAuth authorizations: (optional) The authorization details.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr dict inputs: (optional) The input variables for configuration definition
          and environment.
    :attr ProjectComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    """

    def __init__(
        self,
        name: str,
        *,
        description: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        inputs: dict = None,
        compliance_profile: 'ProjectComplianceProfile' = None,
    ) -> None:
        """
        Initialize a EnvironmentDefinitionRequiredProperties object.

        :param str name: The name of the environment.  It is unique within the
               account across projects and regions.
        :param str description: (optional) The description of the environment.
        :param ProjectConfigAuth authorizations: (optional) The authorization
               details. You can authorize by using a trusted profile or an API key in
               Secrets Manager.
        :param dict inputs: (optional) The input variables for configuration
               definition and environment.
        :param ProjectComplianceProfile compliance_profile: (optional) The profile
               required for compliance.
        """
        self.name = name
        self.description = description
        self.authorizations = authorizations
        self.inputs = inputs
        self.compliance_profile = compliance_profile

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentDefinitionRequiredProperties':
        """Initialize a EnvironmentDefinitionRequiredProperties object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in EnvironmentDefinitionRequiredProperties JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'inputs' in _dict:
            args['inputs'] = _dict.get('inputs')
        if 'compliance_profile' in _dict:
            args['compliance_profile'] = ProjectComplianceProfile.from_dict(_dict.get('compliance_profile'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentDefinitionRequiredProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'authorizations') and self.authorizations is not None:
            if isinstance(self.authorizations, dict):
                _dict['authorizations'] = self.authorizations
            else:
                _dict['authorizations'] = self.authorizations.to_dict()
        if hasattr(self, 'inputs') and self.inputs is not None:
            _dict['inputs'] = self.inputs
        if hasattr(self, 'compliance_profile') and self.compliance_profile is not None:
            if isinstance(self.compliance_profile, dict):
                _dict['compliance_profile'] = self.compliance_profile
            else:
                _dict['compliance_profile'] = self.compliance_profile.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvironmentDefinitionRequiredProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentDefinitionRequiredProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentDefinitionRequiredProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnvironmentDeleteResponse:
    """
    The delete environment response.

    :attr str id: The environment id as a friendly name.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a EnvironmentDeleteResponse object.

        :param str id: The environment id as a friendly name.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentDeleteResponse':
        """Initialize a EnvironmentDeleteResponse object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in EnvironmentDeleteResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentDeleteResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvironmentDeleteResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentDeleteResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentDeleteResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnvironmentPrototype:
    """
    The definition of a project environment.

    :attr EnvironmentDefinitionRequiredProperties definition: The environment
          definition.
    """

    def __init__(
        self,
        definition: 'EnvironmentDefinitionRequiredProperties',
    ) -> None:
        """
        Initialize a EnvironmentPrototype object.

        :param EnvironmentDefinitionRequiredProperties definition: The environment
               definition.
        """
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentPrototype':
        """Initialize a EnvironmentPrototype object from a json dictionary."""
        args = {}
        if 'definition' in _dict:
            args['definition'] = EnvironmentDefinitionRequiredProperties.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in EnvironmentPrototype JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvironmentPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LastActionWithSummary:
    """
    The action job performed on the project configuration.

    :attr str href: A URL.
    :attr str result: (optional) The result of the last action.
    :attr PrePostActionJobWithIdAndSummary pre_job: (optional) A brief summary of a
          pre/post action.
    :attr PrePostActionJobWithIdAndSummary post_job: (optional) A brief summary of a
          pre/post action.
    :attr ActionJobWithIdAndSummary job: (optional) A brief summary of an action.
    """

    def __init__(
        self,
        href: str,
        *,
        result: str = None,
        pre_job: 'PrePostActionJobWithIdAndSummary' = None,
        post_job: 'PrePostActionJobWithIdAndSummary' = None,
        job: 'ActionJobWithIdAndSummary' = None,
    ) -> None:
        """
        Initialize a LastActionWithSummary object.

        :param str href: A URL.
        :param str result: (optional) The result of the last action.
        :param PrePostActionJobWithIdAndSummary pre_job: (optional) A brief summary
               of a pre/post action.
        :param PrePostActionJobWithIdAndSummary post_job: (optional) A brief
               summary of a pre/post action.
        :param ActionJobWithIdAndSummary job: (optional) A brief summary of an
               action.
        """
        self.href = href
        self.result = result
        self.pre_job = pre_job
        self.post_job = post_job
        self.job = job

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LastActionWithSummary':
        """Initialize a LastActionWithSummary object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in LastActionWithSummary JSON')
        if 'result' in _dict:
            args['result'] = _dict.get('result')
        if 'pre_job' in _dict:
            args['pre_job'] = PrePostActionJobWithIdAndSummary.from_dict(_dict.get('pre_job'))
        if 'post_job' in _dict:
            args['post_job'] = PrePostActionJobWithIdAndSummary.from_dict(_dict.get('post_job'))
        if 'job' in _dict:
            args['job'] = ActionJobWithIdAndSummary.from_dict(_dict.get('job'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LastActionWithSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result
        if hasattr(self, 'pre_job') and self.pre_job is not None:
            if isinstance(self.pre_job, dict):
                _dict['pre_job'] = self.pre_job
            else:
                _dict['pre_job'] = self.pre_job.to_dict()
        if hasattr(self, 'post_job') and self.post_job is not None:
            if isinstance(self.post_job, dict):
                _dict['post_job'] = self.post_job
            else:
                _dict['post_job'] = self.post_job.to_dict()
        if hasattr(self, 'job') and self.job is not None:
            if isinstance(self.job, dict):
                _dict['job'] = self.job
            else:
                _dict['job'] = self.job.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LastActionWithSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LastActionWithSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LastActionWithSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResultEnum(str, Enum):
        """
        The result of the last action.
        """

        FAILED = 'failed'
        PASSED = 'passed'


class LastValidatedActionWithSummary:
    """
    The action job performed on the project configuration.

    :attr str href: A URL.
    :attr str result: (optional) The result of the last action.
    :attr PrePostActionJobWithIdAndSummary pre_job: (optional) A brief summary of a
          pre/post action.
    :attr PrePostActionJobWithIdAndSummary post_job: (optional) A brief summary of a
          pre/post action.
    :attr ActionJobWithIdAndSummary job: (optional) A brief summary of an action.
    :attr ProjectConfigMetadataCostEstimate cost_estimate: (optional) The cost
          estimate of the configuration.
          It only exists after the first configuration validation.
    :attr ProjectConfigMetadataCodeRiskAnalyzerLogs cra_logs: (optional) The Code
          Risk Analyzer logs of the configuration.
    """

    def __init__(
        self,
        href: str,
        *,
        result: str = None,
        pre_job: 'PrePostActionJobWithIdAndSummary' = None,
        post_job: 'PrePostActionJobWithIdAndSummary' = None,
        job: 'ActionJobWithIdAndSummary' = None,
        cost_estimate: 'ProjectConfigMetadataCostEstimate' = None,
        cra_logs: 'ProjectConfigMetadataCodeRiskAnalyzerLogs' = None,
    ) -> None:
        """
        Initialize a LastValidatedActionWithSummary object.

        :param str href: A URL.
        :param str result: (optional) The result of the last action.
        :param PrePostActionJobWithIdAndSummary pre_job: (optional) A brief summary
               of a pre/post action.
        :param PrePostActionJobWithIdAndSummary post_job: (optional) A brief
               summary of a pre/post action.
        :param ActionJobWithIdAndSummary job: (optional) A brief summary of an
               action.
        :param ProjectConfigMetadataCostEstimate cost_estimate: (optional) The cost
               estimate of the configuration.
               It only exists after the first configuration validation.
        :param ProjectConfigMetadataCodeRiskAnalyzerLogs cra_logs: (optional) The
               Code Risk Analyzer logs of the configuration.
        """
        self.href = href
        self.result = result
        self.pre_job = pre_job
        self.post_job = post_job
        self.job = job
        self.cost_estimate = cost_estimate
        self.cra_logs = cra_logs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LastValidatedActionWithSummary':
        """Initialize a LastValidatedActionWithSummary object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in LastValidatedActionWithSummary JSON')
        if 'result' in _dict:
            args['result'] = _dict.get('result')
        if 'pre_job' in _dict:
            args['pre_job'] = PrePostActionJobWithIdAndSummary.from_dict(_dict.get('pre_job'))
        if 'post_job' in _dict:
            args['post_job'] = PrePostActionJobWithIdAndSummary.from_dict(_dict.get('post_job'))
        if 'job' in _dict:
            args['job'] = ActionJobWithIdAndSummary.from_dict(_dict.get('job'))
        if 'cost_estimate' in _dict:
            args['cost_estimate'] = ProjectConfigMetadataCostEstimate.from_dict(_dict.get('cost_estimate'))
        if 'cra_logs' in _dict:
            args['cra_logs'] = ProjectConfigMetadataCodeRiskAnalyzerLogs.from_dict(_dict.get('cra_logs'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LastValidatedActionWithSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result
        if hasattr(self, 'pre_job') and self.pre_job is not None:
            if isinstance(self.pre_job, dict):
                _dict['pre_job'] = self.pre_job
            else:
                _dict['pre_job'] = self.pre_job.to_dict()
        if hasattr(self, 'post_job') and self.post_job is not None:
            if isinstance(self.post_job, dict):
                _dict['post_job'] = self.post_job
            else:
                _dict['post_job'] = self.post_job.to_dict()
        if hasattr(self, 'job') and self.job is not None:
            if isinstance(self.job, dict):
                _dict['job'] = self.job
            else:
                _dict['job'] = self.job.to_dict()
        if hasattr(self, 'cost_estimate') and self.cost_estimate is not None:
            if isinstance(self.cost_estimate, dict):
                _dict['cost_estimate'] = self.cost_estimate
            else:
                _dict['cost_estimate'] = self.cost_estimate.to_dict()
        if hasattr(self, 'cra_logs') and self.cra_logs is not None:
            if isinstance(self.cra_logs, dict):
                _dict['cra_logs'] = self.cra_logs
            else:
                _dict['cra_logs'] = self.cra_logs.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LastValidatedActionWithSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LastValidatedActionWithSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LastValidatedActionWithSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResultEnum(str, Enum):
        """
        The result of the last action.
        """

        FAILED = 'failed'
        PASSED = 'passed'


class OutputValue:
    """
    OutputValue.

    :attr str name: The variable name.
    :attr str description: (optional) A short explanation of the output value.
    :attr dict value: (optional) Can be any value - a string, number, boolean,
          array, or object.
    """

    def __init__(
        self,
        name: str,
        *,
        description: str = None,
        value: dict = None,
    ) -> None:
        """
        Initialize a OutputValue object.

        :param str name: The variable name.
        :param str description: (optional) A short explanation of the output value.
        :param dict value: (optional) Can be any value - a string, number, boolean,
               array, or object.
        """
        self.name = name
        self.description = description
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OutputValue':
        """Initialize a OutputValue object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in OutputValue JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OutputValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OutputValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OutputValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OutputValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PaginationLink:
    """
    A pagination link.

    :attr str href: A URL.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a PaginationLink object.

        :param str href: A URL.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PaginationLink':
        """Initialize a PaginationLink object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in PaginationLink JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PaginationLink object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PaginationLink object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PaginationLink') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PaginationLink') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PrePostActionJobSummary:
    """
    A brief summary of a pre/post action job.

    :attr str job_id: The ID of the Schematics action job that ran as part of the
          pre/post job.
    :attr datetime start_time: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr datetime end_time: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr int tasks: (optional) The number of tasks run in the job.
    :attr int ok: (optional) The number of tasks that successfully ran in the job.
    :attr int failed: (optional) The number of tasks that failed in the job.
    :attr int skipped: (optional) The number of tasks that were skipped in the job.
    :attr int changed: (optional) The number of tasks that were changed in the job.
    :attr PrePostActionJobSystemError project_error: (optional) A system-level error
          from the pipeline that ran for this specific pre- and post-job.
    """

    def __init__(
        self,
        job_id: str,
        *,
        start_time: datetime = None,
        end_time: datetime = None,
        tasks: int = None,
        ok: int = None,
        failed: int = None,
        skipped: int = None,
        changed: int = None,
        project_error: 'PrePostActionJobSystemError' = None,
    ) -> None:
        """
        Initialize a PrePostActionJobSummary object.

        :param str job_id: The ID of the Schematics action job that ran as part of
               the pre/post job.
        :param datetime start_time: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param datetime end_time: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param int tasks: (optional) The number of tasks run in the job.
        :param int ok: (optional) The number of tasks that successfully ran in the
               job.
        :param int failed: (optional) The number of tasks that failed in the job.
        :param int skipped: (optional) The number of tasks that were skipped in the
               job.
        :param int changed: (optional) The number of tasks that were changed in the
               job.
        :param PrePostActionJobSystemError project_error: (optional) A system-level
               error from the pipeline that ran for this specific pre- and post-job.
        """
        self.job_id = job_id
        self.start_time = start_time
        self.end_time = end_time
        self.tasks = tasks
        self.ok = ok
        self.failed = failed
        self.skipped = skipped
        self.changed = changed
        self.project_error = project_error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PrePostActionJobSummary':
        """Initialize a PrePostActionJobSummary object from a json dictionary."""
        args = {}
        if 'job_id' in _dict:
            args['job_id'] = _dict.get('job_id')
        else:
            raise ValueError('Required property \'job_id\' not present in PrePostActionJobSummary JSON')
        if 'start_time' in _dict:
            args['start_time'] = string_to_datetime(_dict.get('start_time'))
        if 'end_time' in _dict:
            args['end_time'] = string_to_datetime(_dict.get('end_time'))
        if 'tasks' in _dict:
            args['tasks'] = _dict.get('tasks')
        if 'ok' in _dict:
            args['ok'] = _dict.get('ok')
        if 'failed' in _dict:
            args['failed'] = _dict.get('failed')
        if 'skipped' in _dict:
            args['skipped'] = _dict.get('skipped')
        if 'changed' in _dict:
            args['changed'] = _dict.get('changed')
        if 'project_error' in _dict:
            args['project_error'] = PrePostActionJobSystemError.from_dict(_dict.get('project_error'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PrePostActionJobSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'job_id') and self.job_id is not None:
            _dict['job_id'] = self.job_id
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = datetime_to_string(self.start_time)
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = datetime_to_string(self.end_time)
        if hasattr(self, 'tasks') and self.tasks is not None:
            _dict['tasks'] = self.tasks
        if hasattr(self, 'ok') and self.ok is not None:
            _dict['ok'] = self.ok
        if hasattr(self, 'failed') and self.failed is not None:
            _dict['failed'] = self.failed
        if hasattr(self, 'skipped') and self.skipped is not None:
            _dict['skipped'] = self.skipped
        if hasattr(self, 'changed') and self.changed is not None:
            _dict['changed'] = self.changed
        if hasattr(self, 'project_error') and self.project_error is not None:
            if isinstance(self.project_error, dict):
                _dict['project_error'] = self.project_error
            else:
                _dict['project_error'] = self.project_error.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PrePostActionJobSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PrePostActionJobSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PrePostActionJobSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PrePostActionJobSystemError:
    """
    System level error captured in the Projects Pipelines for pre/post job.

    :attr datetime timestamp: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr str user_id: Id of user that triggered pipeline that ran pre/post job.
    :attr str status_code: HTTP status code for the error.
    :attr str description: Summary description of the error.
    :attr str error_response: (optional) Detailed message from the source error.
    """

    def __init__(
        self,
        timestamp: datetime,
        user_id: str,
        status_code: str,
        description: str,
        *,
        error_response: str = None,
    ) -> None:
        """
        Initialize a PrePostActionJobSystemError object.

        :param datetime timestamp: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param str user_id: Id of user that triggered pipeline that ran pre/post
               job.
        :param str status_code: HTTP status code for the error.
        :param str description: Summary description of the error.
        :param str error_response: (optional) Detailed message from the source
               error.
        """
        self.timestamp = timestamp
        self.user_id = user_id
        self.status_code = status_code
        self.description = description
        self.error_response = error_response

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PrePostActionJobSystemError':
        """Initialize a PrePostActionJobSystemError object from a json dictionary."""
        args = {}
        if 'timestamp' in _dict:
            args['timestamp'] = string_to_datetime(_dict.get('timestamp'))
        else:
            raise ValueError('Required property \'timestamp\' not present in PrePostActionJobSystemError JSON')
        if 'user_id' in _dict:
            args['user_id'] = _dict.get('user_id')
        else:
            raise ValueError('Required property \'user_id\' not present in PrePostActionJobSystemError JSON')
        if 'status_code' in _dict:
            args['status_code'] = _dict.get('status_code')
        else:
            raise ValueError('Required property \'status_code\' not present in PrePostActionJobSystemError JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in PrePostActionJobSystemError JSON')
        if 'error_response' in _dict:
            args['error_response'] = _dict.get('error_response')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PrePostActionJobSystemError object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'timestamp') and self.timestamp is not None:
            _dict['timestamp'] = datetime_to_string(self.timestamp)
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'error_response') and self.error_response is not None:
            _dict['error_response'] = self.error_response
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PrePostActionJobSystemError object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PrePostActionJobSystemError') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PrePostActionJobSystemError') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PrePostActionJobWithIdAndSummary:
    """
    A brief summary of a pre/post action.

    :attr str id: The unique ID.
    :attr PrePostActionJobSummary summary: A brief summary of a pre/post action job.
    """

    def __init__(
        self,
        id: str,
        summary: 'PrePostActionJobSummary',
    ) -> None:
        """
        Initialize a PrePostActionJobWithIdAndSummary object.

        :param str id: The unique ID.
        :param PrePostActionJobSummary summary: A brief summary of a pre/post
               action job.
        """
        self.id = id
        self.summary = summary

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PrePostActionJobWithIdAndSummary':
        """Initialize a PrePostActionJobWithIdAndSummary object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in PrePostActionJobWithIdAndSummary JSON')
        if 'summary' in _dict:
            args['summary'] = PrePostActionJobSummary.from_dict(_dict.get('summary'))
        else:
            raise ValueError('Required property \'summary\' not present in PrePostActionJobWithIdAndSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PrePostActionJobWithIdAndSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'summary') and self.summary is not None:
            if isinstance(self.summary, dict):
                _dict['summary'] = self.summary
            else:
                _dict['summary'] = self.summary.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PrePostActionJobWithIdAndSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PrePostActionJobWithIdAndSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PrePostActionJobWithIdAndSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Project:
    """
    The canonical schema of a project.

    :attr str crn: An IBM Cloud resource name, which uniquely identifies a resource.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr List[CumulativeNeedsAttention] cumulative_needs_attention_view: The
          cumulative list of needs attention items for a project. If the view is
          successfully retrieved, an array which could be empty is returned.
    :attr bool cumulative_needs_attention_view_error: (optional) True indicates that
          the fetch of the needs attention items failed. It only exists if there was an
          error while retrieving the cumulative needs attention view.
    :attr str id: The unique project ID.
    :attr str location: The IBM Cloud location where a resource is deployed.
    :attr str resource_group_id: The resource group id where the project's data and
          tools are created.
    :attr str state: The project status value.
    :attr str href: A URL.
    :attr str resource_group: The resource group name where the project's data and
          tools are created.
    :attr str event_notifications_crn: (optional) The CRN of the event notifications
          instance if one is connected to this project.
    :attr List[ProjectConfigSummary] configs: The project configurations. These
          configurations are only included in the response of creating a project if a
          configs array is specified in the request payload.
    :attr List[ProjectEnvironmentSummary] environments: The project environments.
          These environments are only included in the response if project environments
          were created on the project.
    :attr ProjectDefinitionProperties definition: The definition of the project.
    """

    def __init__(
        self,
        crn: str,
        created_at: datetime,
        cumulative_needs_attention_view: List['CumulativeNeedsAttention'],
        id: str,
        location: str,
        resource_group_id: str,
        state: str,
        href: str,
        resource_group: str,
        configs: List['ProjectConfigSummary'],
        environments: List['ProjectEnvironmentSummary'],
        definition: 'ProjectDefinitionProperties',
        *,
        cumulative_needs_attention_view_error: bool = None,
        event_notifications_crn: str = None,
    ) -> None:
        """
        Initialize a Project object.

        :param str crn: An IBM Cloud resource name, which uniquely identifies a
               resource.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param List[CumulativeNeedsAttention] cumulative_needs_attention_view: The
               cumulative list of needs attention items for a project. If the view is
               successfully retrieved, an array which could be empty is returned.
        :param str id: The unique project ID.
        :param str location: The IBM Cloud location where a resource is deployed.
        :param str resource_group_id: The resource group id where the project's
               data and tools are created.
        :param str state: The project status value.
        :param str href: A URL.
        :param str resource_group: The resource group name where the project's data
               and tools are created.
        :param List[ProjectConfigSummary] configs: The project configurations.
               These configurations are only included in the response of creating a
               project if a configs array is specified in the request payload.
        :param List[ProjectEnvironmentSummary] environments: The project
               environments. These environments are only included in the response if
               project environments were created on the project.
        :param ProjectDefinitionProperties definition: The definition of the
               project.
        :param bool cumulative_needs_attention_view_error: (optional) True
               indicates that the fetch of the needs attention items failed. It only
               exists if there was an error while retrieving the cumulative needs
               attention view.
        :param str event_notifications_crn: (optional) The CRN of the event
               notifications instance if one is connected to this project.
        """
        self.crn = crn
        self.created_at = created_at
        self.cumulative_needs_attention_view = cumulative_needs_attention_view
        self.cumulative_needs_attention_view_error = cumulative_needs_attention_view_error
        self.id = id
        self.location = location
        self.resource_group_id = resource_group_id
        self.state = state
        self.href = href
        self.resource_group = resource_group
        self.event_notifications_crn = event_notifications_crn
        self.configs = configs
        self.environments = environments
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Project':
        """Initialize a Project object from a json dictionary."""
        args = {}
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in Project JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in Project JSON')
        if 'cumulative_needs_attention_view' in _dict:
            args['cumulative_needs_attention_view'] = [
                CumulativeNeedsAttention.from_dict(v) for v in _dict.get('cumulative_needs_attention_view')
            ]
        else:
            raise ValueError('Required property \'cumulative_needs_attention_view\' not present in Project JSON')
        if 'cumulative_needs_attention_view_error' in _dict:
            args['cumulative_needs_attention_view_error'] = _dict.get('cumulative_needs_attention_view_error')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Project JSON')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        else:
            raise ValueError('Required property \'location\' not present in Project JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in Project JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in Project JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in Project JSON')
        if 'resource_group' in _dict:
            args['resource_group'] = _dict.get('resource_group')
        else:
            raise ValueError('Required property \'resource_group\' not present in Project JSON')
        if 'event_notifications_crn' in _dict:
            args['event_notifications_crn'] = _dict.get('event_notifications_crn')
        if 'configs' in _dict:
            args['configs'] = [ProjectConfigSummary.from_dict(v) for v in _dict.get('configs')]
        else:
            raise ValueError('Required property \'configs\' not present in Project JSON')
        if 'environments' in _dict:
            args['environments'] = [ProjectEnvironmentSummary.from_dict(v) for v in _dict.get('environments')]
        else:
            raise ValueError('Required property \'environments\' not present in Project JSON')
        if 'definition' in _dict:
            args['definition'] = ProjectDefinitionProperties.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in Project JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Project object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'cumulative_needs_attention_view') and self.cumulative_needs_attention_view is not None:
            cumulative_needs_attention_view_list = []
            for v in self.cumulative_needs_attention_view:
                if isinstance(v, dict):
                    cumulative_needs_attention_view_list.append(v)
                else:
                    cumulative_needs_attention_view_list.append(v.to_dict())
            _dict['cumulative_needs_attention_view'] = cumulative_needs_attention_view_list
        if (
            hasattr(self, 'cumulative_needs_attention_view_error')
            and self.cumulative_needs_attention_view_error is not None
        ):
            _dict['cumulative_needs_attention_view_error'] = self.cumulative_needs_attention_view_error
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'resource_group') and self.resource_group is not None:
            _dict['resource_group'] = self.resource_group
        if hasattr(self, 'event_notifications_crn') and self.event_notifications_crn is not None:
            _dict['event_notifications_crn'] = self.event_notifications_crn
        if hasattr(self, 'configs') and self.configs is not None:
            configs_list = []
            for v in self.configs:
                if isinstance(v, dict):
                    configs_list.append(v)
                else:
                    configs_list.append(v.to_dict())
            _dict['configs'] = configs_list
        if hasattr(self, 'environments') and self.environments is not None:
            environments_list = []
            for v in self.environments:
                if isinstance(v, dict):
                    environments_list.append(v)
                else:
                    environments_list.append(v.to_dict())
            _dict['environments'] = environments_list
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Project object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Project') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Project') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The project status value.
        """

        READY = 'ready'
        DELETING = 'deleting'
        DELETING_FAILED = 'deleting_failed'


class ProjectCollection:
    """
    Projects list.

    :attr int limit: A pagination limit.
    :attr PaginationLink first: A pagination link.
    :attr PaginationLink next: (optional) A pagination link.
    :attr List[ProjectSummary] projects: (optional) An array of projects.
    """

    def __init__(
        self,
        limit: int,
        first: 'PaginationLink',
        *,
        next: 'PaginationLink' = None,
        projects: List['ProjectSummary'] = None,
    ) -> None:
        """
        Initialize a ProjectCollection object.

        :param int limit: A pagination limit.
        :param PaginationLink first: A pagination link.
        :param PaginationLink next: (optional) A pagination link.
        :param List[ProjectSummary] projects: (optional) An array of projects.
        """
        self.limit = limit
        self.first = first
        self.next = next
        self.projects = projects

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectCollection':
        """Initialize a ProjectCollection object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ProjectCollection JSON')
        if 'first' in _dict:
            args['first'] = PaginationLink.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ProjectCollection JSON')
        if 'next' in _dict:
            args['next'] = PaginationLink.from_dict(_dict.get('next'))
        if 'projects' in _dict:
            args['projects'] = [ProjectSummary.from_dict(v) for v in _dict.get('projects')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'projects') and self.projects is not None:
            projects_list = []
            for v in self.projects:
                if isinstance(v, dict):
                    projects_list.append(v)
                else:
                    projects_list.append(v.to_dict())
            _dict['projects'] = projects_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectComplianceProfile:
    """
    The profile required for compliance.

    :attr str id: (optional) The unique ID for that compliance profile.
    :attr str instance_id: (optional) A unique ID for an instance of a compliance
          profile.
    :attr str instance_location: (optional) The location of the compliance instance.
    :attr str attachment_id: (optional) A unique ID for the attachment to a
          compliance profile.
    :attr str profile_name: (optional) The name of the compliance profile.
    """

    def __init__(
        self,
        *,
        id: str = None,
        instance_id: str = None,
        instance_location: str = None,
        attachment_id: str = None,
        profile_name: str = None,
    ) -> None:
        """
        Initialize a ProjectComplianceProfile object.

        :param str id: (optional) The unique ID for that compliance profile.
        :param str instance_id: (optional) A unique ID for an instance of a
               compliance profile.
        :param str instance_location: (optional) The location of the compliance
               instance.
        :param str attachment_id: (optional) A unique ID for the attachment to a
               compliance profile.
        :param str profile_name: (optional) The name of the compliance profile.
        """
        self.id = id
        self.instance_id = instance_id
        self.instance_location = instance_location
        self.attachment_id = attachment_id
        self.profile_name = profile_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectComplianceProfile':
        """Initialize a ProjectComplianceProfile object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        if 'instance_location' in _dict:
            args['instance_location'] = _dict.get('instance_location')
        if 'attachment_id' in _dict:
            args['attachment_id'] = _dict.get('attachment_id')
        if 'profile_name' in _dict:
            args['profile_name'] = _dict.get('profile_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectComplianceProfile object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'instance_location') and self.instance_location is not None:
            _dict['instance_location'] = self.instance_location
        if hasattr(self, 'attachment_id') and self.attachment_id is not None:
            _dict['attachment_id'] = self.attachment_id
        if hasattr(self, 'profile_name') and self.profile_name is not None:
            _dict['profile_name'] = self.profile_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectComplianceProfile object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectComplianceProfile') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectComplianceProfile') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfig:
    """
    The canonical schema of a project configuration.

    :attr str id: The ID of the configuration. If this parameter is empty, an ID is
          automatically created for the configuration.
    :attr int version: The version of the configuration.
    :attr bool is_draft: The flag that indicates whether the version of the
          configuration is draft, or active.
    :attr List[dict] needs_attention_state: The needs attention state of a
          configuration.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr datetime modified_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr ProjectConfigMetadataLastApproved last_approved: (optional) The last
          approved metadata of the configuration.
    :attr datetime last_saved_at: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr LastValidatedActionWithSummary last_validated: (optional) The action job
          performed on the project configuration.
    :attr LastActionWithSummary last_deployed: (optional) The action job performed
          on the project configuration.
    :attr LastActionWithSummary last_undeployed: (optional) The action job performed
          on the project configuration.
    :attr List[OutputValue] outputs: The outputs of a Schematics template property.
    :attr ProjectReference project: The project referenced by this resource.
    :attr dict references: (optional) The references used in the config to resolve
          input values.
    :attr SchematicsMetadata schematics: (optional) A schematics workspace
          associated to a project configuration, with scripts.
    :attr str state: The state of the configuration.
    :attr bool update_available: (optional) The flag that indicates whether a
          configuration update is available.
    :attr str href: A URL.
    :attr ProjectConfigResponseDefinition definition:
    :attr ProjectConfigVersionSummary approved_version: (optional) The project
          configuration version.
    :attr ProjectConfigVersionSummary deployed_version: (optional) The project
          configuration version.
    """

    def __init__(
        self,
        id: str,
        version: int,
        is_draft: bool,
        needs_attention_state: List[dict],
        created_at: datetime,
        modified_at: datetime,
        outputs: List['OutputValue'],
        project: 'ProjectReference',
        state: str,
        href: str,
        definition: 'ProjectConfigResponseDefinition',
        *,
        last_approved: 'ProjectConfigMetadataLastApproved' = None,
        last_saved_at: datetime = None,
        last_validated: 'LastValidatedActionWithSummary' = None,
        last_deployed: 'LastActionWithSummary' = None,
        last_undeployed: 'LastActionWithSummary' = None,
        references: dict = None,
        schematics: 'SchematicsMetadata' = None,
        update_available: bool = None,
        approved_version: 'ProjectConfigVersionSummary' = None,
        deployed_version: 'ProjectConfigVersionSummary' = None,
    ) -> None:
        """
        Initialize a ProjectConfig object.

        :param str id: The ID of the configuration. If this parameter is empty, an
               ID is automatically created for the configuration.
        :param int version: The version of the configuration.
        :param bool is_draft: The flag that indicates whether the version of the
               configuration is draft, or active.
        :param List[dict] needs_attention_state: The needs attention state of a
               configuration.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param datetime modified_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param List[OutputValue] outputs: The outputs of a Schematics template
               property.
        :param ProjectReference project: The project referenced by this resource.
        :param str state: The state of the configuration.
        :param str href: A URL.
        :param ProjectConfigResponseDefinition definition:
        :param ProjectConfigMetadataLastApproved last_approved: (optional) The last
               approved metadata of the configuration.
        :param datetime last_saved_at: (optional) A date and time value in the
               format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date
               and time format as specified by RFC 3339.
        :param LastValidatedActionWithSummary last_validated: (optional) The action
               job performed on the project configuration.
        :param LastActionWithSummary last_deployed: (optional) The action job
               performed on the project configuration.
        :param LastActionWithSummary last_undeployed: (optional) The action job
               performed on the project configuration.
        :param dict references: (optional) The references used in the config to
               resolve input values.
        :param SchematicsMetadata schematics: (optional) A schematics workspace
               associated to a project configuration, with scripts.
        :param bool update_available: (optional) The flag that indicates whether a
               configuration update is available.
        :param ProjectConfigVersionSummary approved_version: (optional) The project
               configuration version.
        :param ProjectConfigVersionSummary deployed_version: (optional) The project
               configuration version.
        """
        self.id = id
        self.version = version
        self.is_draft = is_draft
        self.needs_attention_state = needs_attention_state
        self.created_at = created_at
        self.modified_at = modified_at
        self.last_approved = last_approved
        self.last_saved_at = last_saved_at
        self.last_validated = last_validated
        self.last_deployed = last_deployed
        self.last_undeployed = last_undeployed
        self.outputs = outputs
        self.project = project
        self.references = references
        self.schematics = schematics
        self.state = state
        self.update_available = update_available
        self.href = href
        self.definition = definition
        self.approved_version = approved_version
        self.deployed_version = deployed_version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfig':
        """Initialize a ProjectConfig object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectConfig JSON')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in ProjectConfig JSON')
        if 'is_draft' in _dict:
            args['is_draft'] = _dict.get('is_draft')
        else:
            raise ValueError('Required property \'is_draft\' not present in ProjectConfig JSON')
        if 'needs_attention_state' in _dict:
            args['needs_attention_state'] = _dict.get('needs_attention_state')
        else:
            raise ValueError('Required property \'needs_attention_state\' not present in ProjectConfig JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProjectConfig JSON')
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        else:
            raise ValueError('Required property \'modified_at\' not present in ProjectConfig JSON')
        if 'last_approved' in _dict:
            args['last_approved'] = ProjectConfigMetadataLastApproved.from_dict(_dict.get('last_approved'))
        if 'last_saved_at' in _dict:
            args['last_saved_at'] = string_to_datetime(_dict.get('last_saved_at'))
        if 'last_validated' in _dict:
            args['last_validated'] = LastValidatedActionWithSummary.from_dict(_dict.get('last_validated'))
        if 'last_deployed' in _dict:
            args['last_deployed'] = LastActionWithSummary.from_dict(_dict.get('last_deployed'))
        if 'last_undeployed' in _dict:
            args['last_undeployed'] = LastActionWithSummary.from_dict(_dict.get('last_undeployed'))
        if 'outputs' in _dict:
            args['outputs'] = [OutputValue.from_dict(v) for v in _dict.get('outputs')]
        else:
            raise ValueError('Required property \'outputs\' not present in ProjectConfig JSON')
        if 'project' in _dict:
            args['project'] = ProjectReference.from_dict(_dict.get('project'))
        else:
            raise ValueError('Required property \'project\' not present in ProjectConfig JSON')
        if 'references' in _dict:
            args['references'] = _dict.get('references')
        if 'schematics' in _dict:
            args['schematics'] = SchematicsMetadata.from_dict(_dict.get('schematics'))
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectConfig JSON')
        if 'update_available' in _dict:
            args['update_available'] = _dict.get('update_available')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ProjectConfig JSON')
        if 'definition' in _dict:
            args['definition'] = _dict.get('definition')
        else:
            raise ValueError('Required property \'definition\' not present in ProjectConfig JSON')
        if 'approved_version' in _dict:
            args['approved_version'] = ProjectConfigVersionSummary.from_dict(_dict.get('approved_version'))
        if 'deployed_version' in _dict:
            args['deployed_version'] = ProjectConfigVersionSummary.from_dict(_dict.get('deployed_version'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfig object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'is_draft') and self.is_draft is not None:
            _dict['is_draft'] = self.is_draft
        if hasattr(self, 'needs_attention_state') and self.needs_attention_state is not None:
            _dict['needs_attention_state'] = self.needs_attention_state
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'modified_at') and self.modified_at is not None:
            _dict['modified_at'] = datetime_to_string(self.modified_at)
        if hasattr(self, 'last_approved') and self.last_approved is not None:
            if isinstance(self.last_approved, dict):
                _dict['last_approved'] = self.last_approved
            else:
                _dict['last_approved'] = self.last_approved.to_dict()
        if hasattr(self, 'last_saved_at') and self.last_saved_at is not None:
            _dict['last_saved_at'] = datetime_to_string(self.last_saved_at)
        if hasattr(self, 'last_validated') and self.last_validated is not None:
            if isinstance(self.last_validated, dict):
                _dict['last_validated'] = self.last_validated
            else:
                _dict['last_validated'] = self.last_validated.to_dict()
        if hasattr(self, 'last_deployed') and self.last_deployed is not None:
            if isinstance(self.last_deployed, dict):
                _dict['last_deployed'] = self.last_deployed
            else:
                _dict['last_deployed'] = self.last_deployed.to_dict()
        if hasattr(self, 'last_undeployed') and self.last_undeployed is not None:
            if isinstance(self.last_undeployed, dict):
                _dict['last_undeployed'] = self.last_undeployed
            else:
                _dict['last_undeployed'] = self.last_undeployed.to_dict()
        if hasattr(self, 'outputs') and self.outputs is not None:
            outputs_list = []
            for v in self.outputs:
                if isinstance(v, dict):
                    outputs_list.append(v)
                else:
                    outputs_list.append(v.to_dict())
            _dict['outputs'] = outputs_list
        if hasattr(self, 'project') and self.project is not None:
            if isinstance(self.project, dict):
                _dict['project'] = self.project
            else:
                _dict['project'] = self.project.to_dict()
        if hasattr(self, 'references') and self.references is not None:
            _dict['references'] = self.references
        if hasattr(self, 'schematics') and self.schematics is not None:
            if isinstance(self.schematics, dict):
                _dict['schematics'] = self.schematics
            else:
                _dict['schematics'] = self.schematics.to_dict()
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'update_available') and self.update_available is not None:
            _dict['update_available'] = self.update_available
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        if hasattr(self, 'approved_version') and self.approved_version is not None:
            if isinstance(self.approved_version, dict):
                _dict['approved_version'] = self.approved_version
            else:
                _dict['approved_version'] = self.approved_version.to_dict()
        if hasattr(self, 'deployed_version') and self.deployed_version is not None:
            if isinstance(self.deployed_version, dict):
                _dict['deployed_version'] = self.deployed_version
            else:
                _dict['deployed_version'] = self.deployed_version.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfig object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfig') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfig') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of the configuration.
        """

        APPROVED = 'approved'
        DELETED = 'deleted'
        DELETING = 'deleting'
        DELETING_FAILED = 'deleting_failed'
        DISCARDED = 'discarded'
        DRAFT = 'draft'
        DEPLOYED = 'deployed'
        DEPLOYING_FAILED = 'deploying_failed'
        DEPLOYING = 'deploying'
        SUPERSEDED = 'superseded'
        UNDEPLOYING = 'undeploying'
        UNDEPLOYING_FAILED = 'undeploying_failed'
        VALIDATED = 'validated'
        VALIDATING = 'validating'
        VALIDATING_FAILED = 'validating_failed'
        APPLIED = 'applied'
        APPLY_FAILED = 'apply_failed'


class ProjectConfigAuth:
    """
    The authorization details. You can authorize by using a trusted profile or an API key
    in Secrets Manager.

    :attr str trusted_profile_id: (optional) The trusted profile ID.
    :attr str method: (optional) The authorization method. You can authorize by
          using a trusted profile or an API key in Secrets Manager.
    :attr str api_key: (optional) The IBM Cloud API Key.
    """

    def __init__(
        self,
        *,
        trusted_profile_id: str = None,
        method: str = None,
        api_key: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigAuth object.

        :param str trusted_profile_id: (optional) The trusted profile ID.
        :param str method: (optional) The authorization method. You can authorize
               by using a trusted profile or an API key in Secrets Manager.
        :param str api_key: (optional) The IBM Cloud API Key.
        """
        self.trusted_profile_id = trusted_profile_id
        self.method = method
        self.api_key = api_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigAuth':
        """Initialize a ProjectConfigAuth object from a json dictionary."""
        args = {}
        if 'trusted_profile_id' in _dict:
            args['trusted_profile_id'] = _dict.get('trusted_profile_id')
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'api_key' in _dict:
            args['api_key'] = _dict.get('api_key')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigAuth object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'trusted_profile_id') and self.trusted_profile_id is not None:
            _dict['trusted_profile_id'] = self.trusted_profile_id
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'api_key') and self.api_key is not None:
            _dict['api_key'] = self.api_key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigAuth object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigAuth') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigAuth') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MethodEnum(str, Enum):
        """
        The authorization method. You can authorize by using a trusted profile or an API
        key in Secrets Manager.
        """

        API_KEY = 'api_key'
        TRUSTED_PROFILE = 'trusted_profile'


class ProjectConfigCollection:
    """
    The project configuration list.

    :attr List[ProjectConfigSummary] configs: (optional) The collection list
          operation response schema that should define the array property with the name
          "configs".
    """

    def __init__(
        self,
        *,
        configs: List['ProjectConfigSummary'] = None,
    ) -> None:
        """
        Initialize a ProjectConfigCollection object.

        :param List[ProjectConfigSummary] configs: (optional) The collection list
               operation response schema that should define the array property with the
               name "configs".
        """
        self.configs = configs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigCollection':
        """Initialize a ProjectConfigCollection object from a json dictionary."""
        args = {}
        if 'configs' in _dict:
            args['configs'] = [ProjectConfigSummary.from_dict(v) for v in _dict.get('configs')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'configs') and self.configs is not None:
            configs_list = []
            for v in self.configs:
                if isinstance(v, dict):
                    configs_list.append(v)
                else:
                    configs_list.append(v.to_dict())
            _dict['configs'] = configs_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigDefinitionNameDescription:
    """
    The name and description of a project configuration.

    :attr str name: (optional) The configuration name. It is unique within the
          account across projects and regions.
    :attr str description: (optional) A project configuration description.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigDefinitionNameDescription object.

        :param str name: (optional) The configuration name. It is unique within the
               account across projects and regions.
        :param str description: (optional) A project configuration description.
        """
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigDefinitionNameDescription':
        """Initialize a ProjectConfigDefinitionNameDescription object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigDefinitionNameDescription object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigDefinitionNameDescription object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigDefinitionNameDescription') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigDefinitionNameDescription') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigDelete:
    """
    Deletes the configuration response.

    :attr str id: The unique configuration ID.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a ProjectConfigDelete object.

        :param str id: The unique configuration ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigDelete':
        """Initialize a ProjectConfigDelete object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectConfigDelete JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigDelete object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigDelete object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigDelete') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigDelete') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigMetadataCodeRiskAnalyzerLogs:
    """
    The Code Risk Analyzer logs of the configuration.

    :attr str cra_version: (optional) The version of the Code Risk Analyzer logs of
          the configuration. This will change as the Code Risk Analyzer is updated.
    :attr str schema_version: (optional) The schema version of Code Risk Analyzer
          logs of the configuration.
    :attr str status: (optional) The status of the Code Risk Analyzer logs of the
          configuration.
    :attr CodeRiskAnalyzerLogsSummary summary: (optional) The Code Risk Analyzer
          logs summary of the configuration.
    :attr datetime timestamp: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    """

    def __init__(
        self,
        *,
        cra_version: str = None,
        schema_version: str = None,
        status: str = None,
        summary: 'CodeRiskAnalyzerLogsSummary' = None,
        timestamp: datetime = None,
    ) -> None:
        """
        Initialize a ProjectConfigMetadataCodeRiskAnalyzerLogs object.

        :param str cra_version: (optional) The version of the Code Risk Analyzer
               logs of the configuration. This will change as the Code Risk Analyzer is
               updated.
        :param str schema_version: (optional) The schema version of Code Risk
               Analyzer logs of the configuration.
        :param str status: (optional) The status of the Code Risk Analyzer logs of
               the configuration.
        :param CodeRiskAnalyzerLogsSummary summary: (optional) The Code Risk
               Analyzer logs summary of the configuration.
        :param datetime timestamp: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        """
        self.cra_version = cra_version
        self.schema_version = schema_version
        self.status = status
        self.summary = summary
        self.timestamp = timestamp

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigMetadataCodeRiskAnalyzerLogs':
        """Initialize a ProjectConfigMetadataCodeRiskAnalyzerLogs object from a json dictionary."""
        args = {}
        if 'cra_version' in _dict:
            args['cra_version'] = _dict.get('cra_version')
        if 'schema_version' in _dict:
            args['schema_version'] = _dict.get('schema_version')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'summary' in _dict:
            args['summary'] = CodeRiskAnalyzerLogsSummary.from_dict(_dict.get('summary'))
        if 'timestamp' in _dict:
            args['timestamp'] = string_to_datetime(_dict.get('timestamp'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigMetadataCodeRiskAnalyzerLogs object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cra_version') and self.cra_version is not None:
            _dict['cra_version'] = self.cra_version
        if hasattr(self, 'schema_version') and self.schema_version is not None:
            _dict['schema_version'] = self.schema_version
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'summary') and self.summary is not None:
            if isinstance(self.summary, dict):
                _dict['summary'] = self.summary
            else:
                _dict['summary'] = self.summary.to_dict()
        if hasattr(self, 'timestamp') and self.timestamp is not None:
            _dict['timestamp'] = datetime_to_string(self.timestamp)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigMetadataCodeRiskAnalyzerLogs object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigMetadataCodeRiskAnalyzerLogs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigMetadataCodeRiskAnalyzerLogs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of the Code Risk Analyzer logs of the configuration.
        """

        PASSED = 'passed'
        FAILED = 'failed'


class ProjectConfigMetadataCostEstimate:
    """
    The cost estimate of the configuration. It only exists after the first configuration
    validation.

    :attr str version: (optional) The version of the cost estimate of the
          configuration.
    :attr str currency: (optional) The currency of the cost estimate of the
          configuration.
    :attr str total_hourly_cost: (optional) The total hourly cost estimate of the
          configuration.
    :attr str total_monthly_cost: (optional) The total monthly cost estimate of the
          configuration.
    :attr str past_total_hourly_cost: (optional) The past total hourly cost estimate
          of the configuration.
    :attr str past_total_monthly_cost: (optional) The past total monthly cost
          estimate of the configuration.
    :attr str diff_total_hourly_cost: (optional) The difference between current and
          past total hourly cost estimates of the configuration.
    :attr str diff_total_monthly_cost: (optional) The difference between current and
          past total monthly cost estimates of the configuration.
    :attr datetime time_generated: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr str user_id: (optional) The unique ID.
    """

    def __init__(
        self,
        *,
        version: str = None,
        currency: str = None,
        total_hourly_cost: str = None,
        total_monthly_cost: str = None,
        past_total_hourly_cost: str = None,
        past_total_monthly_cost: str = None,
        diff_total_hourly_cost: str = None,
        diff_total_monthly_cost: str = None,
        time_generated: datetime = None,
        user_id: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigMetadataCostEstimate object.

        :param str version: (optional) The version of the cost estimate of the
               configuration.
        :param str currency: (optional) The currency of the cost estimate of the
               configuration.
        :param str total_hourly_cost: (optional) The total hourly cost estimate of
               the configuration.
        :param str total_monthly_cost: (optional) The total monthly cost estimate
               of the configuration.
        :param str past_total_hourly_cost: (optional) The past total hourly cost
               estimate of the configuration.
        :param str past_total_monthly_cost: (optional) The past total monthly cost
               estimate of the configuration.
        :param str diff_total_hourly_cost: (optional) The difference between
               current and past total hourly cost estimates of the configuration.
        :param str diff_total_monthly_cost: (optional) The difference between
               current and past total monthly cost estimates of the configuration.
        :param datetime time_generated: (optional) A date and time value in the
               format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date
               and time format as specified by RFC 3339.
        :param str user_id: (optional) The unique ID.
        """
        self.version = version
        self.currency = currency
        self.total_hourly_cost = total_hourly_cost
        self.total_monthly_cost = total_monthly_cost
        self.past_total_hourly_cost = past_total_hourly_cost
        self.past_total_monthly_cost = past_total_monthly_cost
        self.diff_total_hourly_cost = diff_total_hourly_cost
        self.diff_total_monthly_cost = diff_total_monthly_cost
        self.time_generated = time_generated
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigMetadataCostEstimate':
        """Initialize a ProjectConfigMetadataCostEstimate object from a json dictionary."""
        args = {}
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'currency' in _dict:
            args['currency'] = _dict.get('currency')
        if 'totalHourlyCost' in _dict:
            args['total_hourly_cost'] = _dict.get('totalHourlyCost')
        if 'totalMonthlyCost' in _dict:
            args['total_monthly_cost'] = _dict.get('totalMonthlyCost')
        if 'pastTotalHourlyCost' in _dict:
            args['past_total_hourly_cost'] = _dict.get('pastTotalHourlyCost')
        if 'pastTotalMonthlyCost' in _dict:
            args['past_total_monthly_cost'] = _dict.get('pastTotalMonthlyCost')
        if 'diffTotalHourlyCost' in _dict:
            args['diff_total_hourly_cost'] = _dict.get('diffTotalHourlyCost')
        if 'diffTotalMonthlyCost' in _dict:
            args['diff_total_monthly_cost'] = _dict.get('diffTotalMonthlyCost')
        if 'timeGenerated' in _dict:
            args['time_generated'] = string_to_datetime(_dict.get('timeGenerated'))
        if 'user_id' in _dict:
            args['user_id'] = _dict.get('user_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigMetadataCostEstimate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'currency') and self.currency is not None:
            _dict['currency'] = self.currency
        if hasattr(self, 'total_hourly_cost') and self.total_hourly_cost is not None:
            _dict['totalHourlyCost'] = self.total_hourly_cost
        if hasattr(self, 'total_monthly_cost') and self.total_monthly_cost is not None:
            _dict['totalMonthlyCost'] = self.total_monthly_cost
        if hasattr(self, 'past_total_hourly_cost') and self.past_total_hourly_cost is not None:
            _dict['pastTotalHourlyCost'] = self.past_total_hourly_cost
        if hasattr(self, 'past_total_monthly_cost') and self.past_total_monthly_cost is not None:
            _dict['pastTotalMonthlyCost'] = self.past_total_monthly_cost
        if hasattr(self, 'diff_total_hourly_cost') and self.diff_total_hourly_cost is not None:
            _dict['diffTotalHourlyCost'] = self.diff_total_hourly_cost
        if hasattr(self, 'diff_total_monthly_cost') and self.diff_total_monthly_cost is not None:
            _dict['diffTotalMonthlyCost'] = self.diff_total_monthly_cost
        if hasattr(self, 'time_generated') and self.time_generated is not None:
            _dict['timeGenerated'] = datetime_to_string(self.time_generated)
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigMetadataCostEstimate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigMetadataCostEstimate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigMetadataCostEstimate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigMetadataLastApproved:
    """
    The last approved metadata of the configuration.

    :attr datetime at: A date and time value in the format YYYY-MM-DDTHH:mm:ssZ or
          YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time format as specified by RFC
          3339.
    :attr str comment: (optional) The comment left by the user who approved the
          configuration.
    :attr bool is_forced: The flag that indicates whether the approval was forced
          approved.
    :attr str user_id: The unique ID.
    """

    def __init__(
        self,
        at: datetime,
        is_forced: bool,
        user_id: str,
        *,
        comment: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigMetadataLastApproved object.

        :param datetime at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param bool is_forced: The flag that indicates whether the approval was
               forced approved.
        :param str user_id: The unique ID.
        :param str comment: (optional) The comment left by the user who approved
               the configuration.
        """
        self.at = at
        self.comment = comment
        self.is_forced = is_forced
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigMetadataLastApproved':
        """Initialize a ProjectConfigMetadataLastApproved object from a json dictionary."""
        args = {}
        if 'at' in _dict:
            args['at'] = string_to_datetime(_dict.get('at'))
        else:
            raise ValueError('Required property \'at\' not present in ProjectConfigMetadataLastApproved JSON')
        if 'comment' in _dict:
            args['comment'] = _dict.get('comment')
        if 'is_forced' in _dict:
            args['is_forced'] = _dict.get('is_forced')
        else:
            raise ValueError('Required property \'is_forced\' not present in ProjectConfigMetadataLastApproved JSON')
        if 'user_id' in _dict:
            args['user_id'] = _dict.get('user_id')
        else:
            raise ValueError('Required property \'user_id\' not present in ProjectConfigMetadataLastApproved JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigMetadataLastApproved object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'at') and self.at is not None:
            _dict['at'] = datetime_to_string(self.at)
        if hasattr(self, 'comment') and self.comment is not None:
            _dict['comment'] = self.comment
        if hasattr(self, 'is_forced') and self.is_forced is not None:
            _dict['is_forced'] = self.is_forced
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigMetadataLastApproved object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigMetadataLastApproved') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigMetadataLastApproved') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigPatchDefinitionBlock:
    """
    ProjectConfigPatchDefinitionBlock.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a ProjectConfigPatchDefinitionBlock object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(
                [
                    'ProjectConfigPatchDefinitionBlockDAConfigDefinitionProperties',
                    'ProjectConfigPatchDefinitionBlockResourceConfigDefinitionProperties',
                ]
            )
        )
        raise Exception(msg)


class ProjectConfigPrototype:
    """
    The input of a project configuration.

    :attr ProjectConfigPrototypeDefinitionBlock definition:
    :attr SchematicsWorkspace schematics: (optional) A Schematics workspace to use
          for deploying this configuration.
          Either schematics.workspace_crn, definition.locator_id, or both must be
          specified.
    """

    def __init__(
        self,
        definition: 'ProjectConfigPrototypeDefinitionBlock',
        *,
        schematics: 'SchematicsWorkspace' = None,
    ) -> None:
        """
        Initialize a ProjectConfigPrototype object.

        :param ProjectConfigPrototypeDefinitionBlock definition:
        :param SchematicsWorkspace schematics: (optional) A Schematics workspace to
               use for deploying this configuration.
               Either schematics.workspace_crn, definition.locator_id, or both must be
               specified.
        """
        self.definition = definition
        self.schematics = schematics

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigPrototype':
        """Initialize a ProjectConfigPrototype object from a json dictionary."""
        args = {}
        if 'definition' in _dict:
            args['definition'] = _dict.get('definition')
        else:
            raise ValueError('Required property \'definition\' not present in ProjectConfigPrototype JSON')
        if 'schematics' in _dict:
            args['schematics'] = SchematicsWorkspace.from_dict(_dict.get('schematics'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        if hasattr(self, 'schematics') and self.schematics is not None:
            if isinstance(self.schematics, dict):
                _dict['schematics'] = self.schematics
            else:
                _dict['schematics'] = self.schematics.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigPrototypeDefinitionBlock:
    """
    ProjectConfigPrototypeDefinitionBlock.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a ProjectConfigPrototypeDefinitionBlock object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(
                [
                    'ProjectConfigPrototypeDefinitionBlockDAConfigDefinitionProperties',
                    'ProjectConfigPrototypeDefinitionBlockResourceConfigDefinitionProperties',
                ]
            )
        )
        raise Exception(msg)


class ProjectConfigResource:
    """
    ProjectConfigResource.

    :attr str resource_crn: (optional) An IBM Cloud resource name, which uniquely
          identifies a resource.
    :attr str resource_name: (optional) The name of the resource.
    :attr str resource_type: (optional) The resource type.
    :attr bool resource_tainted: (optional) The flag that indicates whether the
          status of the resource is tainted.
    :attr str resource_group_name: (optional) The resource group of the resource.
    """

    def __init__(
        self,
        *,
        resource_crn: str = None,
        resource_name: str = None,
        resource_type: str = None,
        resource_tainted: bool = None,
        resource_group_name: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigResource object.

        :param str resource_crn: (optional) An IBM Cloud resource name, which
               uniquely identifies a resource.
        :param str resource_name: (optional) The name of the resource.
        :param str resource_type: (optional) The resource type.
        :param bool resource_tainted: (optional) The flag that indicates whether
               the status of the resource is tainted.
        :param str resource_group_name: (optional) The resource group of the
               resource.
        """
        self.resource_crn = resource_crn
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.resource_tainted = resource_tainted
        self.resource_group_name = resource_group_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigResource':
        """Initialize a ProjectConfigResource object from a json dictionary."""
        args = {}
        if 'resource_crn' in _dict:
            args['resource_crn'] = _dict.get('resource_crn')
        if 'resource_name' in _dict:
            args['resource_name'] = _dict.get('resource_name')
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        if 'resource_tainted' in _dict:
            args['resource_tainted'] = _dict.get('resource_tainted')
        if 'resource_group_name' in _dict:
            args['resource_group_name'] = _dict.get('resource_group_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigResource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_crn') and self.resource_crn is not None:
            _dict['resource_crn'] = self.resource_crn
        if hasattr(self, 'resource_name') and self.resource_name is not None:
            _dict['resource_name'] = self.resource_name
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'resource_tainted') and self.resource_tainted is not None:
            _dict['resource_tainted'] = self.resource_tainted
        if hasattr(self, 'resource_group_name') and self.resource_group_name is not None:
            _dict['resource_group_name'] = self.resource_group_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigResource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigResource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigResource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigResourceCollection:
    """
    The project configuration resource list.

    :attr List[ProjectConfigResource] resources: The collection list operation
          response schema that defines the array property with the name `resources`.
    :attr int resources_count: The total number of resources deployed by the
          configuration.
    """

    def __init__(
        self,
        resources: List['ProjectConfigResource'],
        resources_count: int,
    ) -> None:
        """
        Initialize a ProjectConfigResourceCollection object.

        :param List[ProjectConfigResource] resources: The collection list operation
               response schema that defines the array property with the name `resources`.
        :param int resources_count: The total number of resources deployed by the
               configuration.
        """
        self.resources = resources
        self.resources_count = resources_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigResourceCollection':
        """Initialize a ProjectConfigResourceCollection object from a json dictionary."""
        args = {}
        if 'resources' in _dict:
            args['resources'] = [ProjectConfigResource.from_dict(v) for v in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in ProjectConfigResourceCollection JSON')
        if 'resources_count' in _dict:
            args['resources_count'] = _dict.get('resources_count')
        else:
            raise ValueError(
                'Required property \'resources_count\' not present in ProjectConfigResourceCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigResourceCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resources') and self.resources is not None:
            resources_list = []
            for v in self.resources:
                if isinstance(v, dict):
                    resources_list.append(v)
                else:
                    resources_list.append(v.to_dict())
            _dict['resources'] = resources_list
        if hasattr(self, 'resources_count') and self.resources_count is not None:
            _dict['resources_count'] = self.resources_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigResourceCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigResourceCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigResourceCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigResponseDefinition:
    """
    ProjectConfigResponseDefinition.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a ProjectConfigResponseDefinition object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(
                [
                    'ProjectConfigResponseDefinitionDAConfigDefinitionProperties',
                    'ProjectConfigResponseDefinitionResourceConfigDefinitionProperties',
                ]
            )
        )
        raise Exception(msg)


class ProjectConfigSummary:
    """
    ProjectConfigSummary.

    :attr ProjectConfigVersionSummary approved_version: (optional) The project
          configuration version.
    :attr ProjectConfigVersionSummary deployed_version: (optional) The project
          configuration version.
    :attr str id: The ID of the configuration. If this parameter is empty, an ID is
          automatically created for the configuration.
    :attr int version: The version of the configuration.
    :attr str state: The state of the configuration.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr datetime modified_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr str href: A URL.
    :attr ProjectConfigDefinitionNameDescription definition: The name and
          description of a project configuration.
    :attr ProjectReference project: The project referenced by this resource.
    :attr str deployment_model: (optional) The configuration type.
    """

    def __init__(
        self,
        id: str,
        version: int,
        state: str,
        created_at: datetime,
        modified_at: datetime,
        href: str,
        definition: 'ProjectConfigDefinitionNameDescription',
        project: 'ProjectReference',
        *,
        approved_version: 'ProjectConfigVersionSummary' = None,
        deployed_version: 'ProjectConfigVersionSummary' = None,
        deployment_model: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigSummary object.

        :param str id: The ID of the configuration. If this parameter is empty, an
               ID is automatically created for the configuration.
        :param int version: The version of the configuration.
        :param str state: The state of the configuration.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param datetime modified_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param str href: A URL.
        :param ProjectConfigDefinitionNameDescription definition: The name and
               description of a project configuration.
        :param ProjectReference project: The project referenced by this resource.
        :param ProjectConfigVersionSummary approved_version: (optional) The project
               configuration version.
        :param ProjectConfigVersionSummary deployed_version: (optional) The project
               configuration version.
        :param str deployment_model: (optional) The configuration type.
        """
        self.approved_version = approved_version
        self.deployed_version = deployed_version
        self.id = id
        self.version = version
        self.state = state
        self.created_at = created_at
        self.modified_at = modified_at
        self.href = href
        self.definition = definition
        self.project = project
        self.deployment_model = deployment_model

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigSummary':
        """Initialize a ProjectConfigSummary object from a json dictionary."""
        args = {}
        if 'approved_version' in _dict:
            args['approved_version'] = ProjectConfigVersionSummary.from_dict(_dict.get('approved_version'))
        if 'deployed_version' in _dict:
            args['deployed_version'] = ProjectConfigVersionSummary.from_dict(_dict.get('deployed_version'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectConfigSummary JSON')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in ProjectConfigSummary JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectConfigSummary JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProjectConfigSummary JSON')
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        else:
            raise ValueError('Required property \'modified_at\' not present in ProjectConfigSummary JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ProjectConfigSummary JSON')
        if 'definition' in _dict:
            args['definition'] = ProjectConfigDefinitionNameDescription.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in ProjectConfigSummary JSON')
        if 'project' in _dict:
            args['project'] = ProjectReference.from_dict(_dict.get('project'))
        else:
            raise ValueError('Required property \'project\' not present in ProjectConfigSummary JSON')
        if 'deployment_model' in _dict:
            args['deployment_model'] = _dict.get('deployment_model')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'approved_version') and self.approved_version is not None:
            if isinstance(self.approved_version, dict):
                _dict['approved_version'] = self.approved_version
            else:
                _dict['approved_version'] = self.approved_version.to_dict()
        if hasattr(self, 'deployed_version') and self.deployed_version is not None:
            if isinstance(self.deployed_version, dict):
                _dict['deployed_version'] = self.deployed_version
            else:
                _dict['deployed_version'] = self.deployed_version.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'modified_at') and self.modified_at is not None:
            _dict['modified_at'] = datetime_to_string(self.modified_at)
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        if hasattr(self, 'project') and self.project is not None:
            if isinstance(self.project, dict):
                _dict['project'] = self.project
            else:
                _dict['project'] = self.project.to_dict()
        if hasattr(self, 'deployment_model') and self.deployment_model is not None:
            _dict['deployment_model'] = self.deployment_model
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of the configuration.
        """

        APPROVED = 'approved'
        DELETED = 'deleted'
        DELETING = 'deleting'
        DELETING_FAILED = 'deleting_failed'
        DISCARDED = 'discarded'
        DRAFT = 'draft'
        DEPLOYED = 'deployed'
        DEPLOYING_FAILED = 'deploying_failed'
        DEPLOYING = 'deploying'
        SUPERSEDED = 'superseded'
        UNDEPLOYING = 'undeploying'
        UNDEPLOYING_FAILED = 'undeploying_failed'
        VALIDATED = 'validated'
        VALIDATING = 'validating'
        VALIDATING_FAILED = 'validating_failed'
        APPLIED = 'applied'
        APPLY_FAILED = 'apply_failed'

    class DeploymentModelEnum(str, Enum):
        """
        The configuration type.
        """

        PROJECT_DEPLOYED = 'project_deployed'
        USER_DEPLOYED = 'user_deployed'


class ProjectConfigVersion:
    """
    A specific version of a project configuration.

    :attr str id: The ID of the configuration. If this parameter is empty, an ID is
          automatically created for the configuration.
    :attr int version: The version of the configuration.
    :attr bool is_draft: The flag that indicates whether the version of the
          configuration is draft, or active.
    :attr List[dict] needs_attention_state: The needs attention state of a
          configuration.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr datetime modified_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr ProjectConfigMetadataLastApproved last_approved: (optional) The last
          approved metadata of the configuration.
    :attr datetime last_saved_at: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr LastValidatedActionWithSummary last_validated: (optional) The action job
          performed on the project configuration.
    :attr LastActionWithSummary last_deployed: (optional) The action job performed
          on the project configuration.
    :attr LastActionWithSummary last_undeployed: (optional) The action job performed
          on the project configuration.
    :attr List[OutputValue] outputs: The outputs of a Schematics template property.
    :attr ProjectReference project: The project referenced by this resource.
    :attr dict references: (optional) The references used in the config to resolve
          input values.
    :attr SchematicsMetadata schematics: (optional) A schematics workspace
          associated to a project configuration, with scripts.
    :attr str state: The state of the configuration.
    :attr bool update_available: (optional) The flag that indicates whether a
          configuration update is available.
    :attr str href: A URL.
    :attr ProjectConfigResponseDefinition definition:
    """

    def __init__(
        self,
        id: str,
        version: int,
        is_draft: bool,
        needs_attention_state: List[dict],
        created_at: datetime,
        modified_at: datetime,
        outputs: List['OutputValue'],
        project: 'ProjectReference',
        state: str,
        href: str,
        definition: 'ProjectConfigResponseDefinition',
        *,
        last_approved: 'ProjectConfigMetadataLastApproved' = None,
        last_saved_at: datetime = None,
        last_validated: 'LastValidatedActionWithSummary' = None,
        last_deployed: 'LastActionWithSummary' = None,
        last_undeployed: 'LastActionWithSummary' = None,
        references: dict = None,
        schematics: 'SchematicsMetadata' = None,
        update_available: bool = None,
    ) -> None:
        """
        Initialize a ProjectConfigVersion object.

        :param str id: The ID of the configuration. If this parameter is empty, an
               ID is automatically created for the configuration.
        :param int version: The version of the configuration.
        :param bool is_draft: The flag that indicates whether the version of the
               configuration is draft, or active.
        :param List[dict] needs_attention_state: The needs attention state of a
               configuration.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param datetime modified_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param List[OutputValue] outputs: The outputs of a Schematics template
               property.
        :param ProjectReference project: The project referenced by this resource.
        :param str state: The state of the configuration.
        :param str href: A URL.
        :param ProjectConfigResponseDefinition definition:
        :param ProjectConfigMetadataLastApproved last_approved: (optional) The last
               approved metadata of the configuration.
        :param datetime last_saved_at: (optional) A date and time value in the
               format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date
               and time format as specified by RFC 3339.
        :param LastValidatedActionWithSummary last_validated: (optional) The action
               job performed on the project configuration.
        :param LastActionWithSummary last_deployed: (optional) The action job
               performed on the project configuration.
        :param LastActionWithSummary last_undeployed: (optional) The action job
               performed on the project configuration.
        :param dict references: (optional) The references used in the config to
               resolve input values.
        :param SchematicsMetadata schematics: (optional) A schematics workspace
               associated to a project configuration, with scripts.
        :param bool update_available: (optional) The flag that indicates whether a
               configuration update is available.
        """
        self.id = id
        self.version = version
        self.is_draft = is_draft
        self.needs_attention_state = needs_attention_state
        self.created_at = created_at
        self.modified_at = modified_at
        self.last_approved = last_approved
        self.last_saved_at = last_saved_at
        self.last_validated = last_validated
        self.last_deployed = last_deployed
        self.last_undeployed = last_undeployed
        self.outputs = outputs
        self.project = project
        self.references = references
        self.schematics = schematics
        self.state = state
        self.update_available = update_available
        self.href = href
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigVersion':
        """Initialize a ProjectConfigVersion object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectConfigVersion JSON')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in ProjectConfigVersion JSON')
        if 'is_draft' in _dict:
            args['is_draft'] = _dict.get('is_draft')
        else:
            raise ValueError('Required property \'is_draft\' not present in ProjectConfigVersion JSON')
        if 'needs_attention_state' in _dict:
            args['needs_attention_state'] = _dict.get('needs_attention_state')
        else:
            raise ValueError('Required property \'needs_attention_state\' not present in ProjectConfigVersion JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProjectConfigVersion JSON')
        if 'modified_at' in _dict:
            args['modified_at'] = string_to_datetime(_dict.get('modified_at'))
        else:
            raise ValueError('Required property \'modified_at\' not present in ProjectConfigVersion JSON')
        if 'last_approved' in _dict:
            args['last_approved'] = ProjectConfigMetadataLastApproved.from_dict(_dict.get('last_approved'))
        if 'last_saved_at' in _dict:
            args['last_saved_at'] = string_to_datetime(_dict.get('last_saved_at'))
        if 'last_validated' in _dict:
            args['last_validated'] = LastValidatedActionWithSummary.from_dict(_dict.get('last_validated'))
        if 'last_deployed' in _dict:
            args['last_deployed'] = LastActionWithSummary.from_dict(_dict.get('last_deployed'))
        if 'last_undeployed' in _dict:
            args['last_undeployed'] = LastActionWithSummary.from_dict(_dict.get('last_undeployed'))
        if 'outputs' in _dict:
            args['outputs'] = [OutputValue.from_dict(v) for v in _dict.get('outputs')]
        else:
            raise ValueError('Required property \'outputs\' not present in ProjectConfigVersion JSON')
        if 'project' in _dict:
            args['project'] = ProjectReference.from_dict(_dict.get('project'))
        else:
            raise ValueError('Required property \'project\' not present in ProjectConfigVersion JSON')
        if 'references' in _dict:
            args['references'] = _dict.get('references')
        if 'schematics' in _dict:
            args['schematics'] = SchematicsMetadata.from_dict(_dict.get('schematics'))
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectConfigVersion JSON')
        if 'update_available' in _dict:
            args['update_available'] = _dict.get('update_available')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ProjectConfigVersion JSON')
        if 'definition' in _dict:
            args['definition'] = _dict.get('definition')
        else:
            raise ValueError('Required property \'definition\' not present in ProjectConfigVersion JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigVersion object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'is_draft') and self.is_draft is not None:
            _dict['is_draft'] = self.is_draft
        if hasattr(self, 'needs_attention_state') and self.needs_attention_state is not None:
            _dict['needs_attention_state'] = self.needs_attention_state
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'modified_at') and self.modified_at is not None:
            _dict['modified_at'] = datetime_to_string(self.modified_at)
        if hasattr(self, 'last_approved') and self.last_approved is not None:
            if isinstance(self.last_approved, dict):
                _dict['last_approved'] = self.last_approved
            else:
                _dict['last_approved'] = self.last_approved.to_dict()
        if hasattr(self, 'last_saved_at') and self.last_saved_at is not None:
            _dict['last_saved_at'] = datetime_to_string(self.last_saved_at)
        if hasattr(self, 'last_validated') and self.last_validated is not None:
            if isinstance(self.last_validated, dict):
                _dict['last_validated'] = self.last_validated
            else:
                _dict['last_validated'] = self.last_validated.to_dict()
        if hasattr(self, 'last_deployed') and self.last_deployed is not None:
            if isinstance(self.last_deployed, dict):
                _dict['last_deployed'] = self.last_deployed
            else:
                _dict['last_deployed'] = self.last_deployed.to_dict()
        if hasattr(self, 'last_undeployed') and self.last_undeployed is not None:
            if isinstance(self.last_undeployed, dict):
                _dict['last_undeployed'] = self.last_undeployed
            else:
                _dict['last_undeployed'] = self.last_undeployed.to_dict()
        if hasattr(self, 'outputs') and self.outputs is not None:
            outputs_list = []
            for v in self.outputs:
                if isinstance(v, dict):
                    outputs_list.append(v)
                else:
                    outputs_list.append(v.to_dict())
            _dict['outputs'] = outputs_list
        if hasattr(self, 'project') and self.project is not None:
            if isinstance(self.project, dict):
                _dict['project'] = self.project
            else:
                _dict['project'] = self.project.to_dict()
        if hasattr(self, 'references') and self.references is not None:
            _dict['references'] = self.references
        if hasattr(self, 'schematics') and self.schematics is not None:
            if isinstance(self.schematics, dict):
                _dict['schematics'] = self.schematics
            else:
                _dict['schematics'] = self.schematics.to_dict()
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'update_available') and self.update_available is not None:
            _dict['update_available'] = self.update_available
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigVersion object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigVersion') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigVersion') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of the configuration.
        """

        APPROVED = 'approved'
        DELETED = 'deleted'
        DELETING = 'deleting'
        DELETING_FAILED = 'deleting_failed'
        DISCARDED = 'discarded'
        DRAFT = 'draft'
        DEPLOYED = 'deployed'
        DEPLOYING_FAILED = 'deploying_failed'
        DEPLOYING = 'deploying'
        SUPERSEDED = 'superseded'
        UNDEPLOYING = 'undeploying'
        UNDEPLOYING_FAILED = 'undeploying_failed'
        VALIDATED = 'validated'
        VALIDATING = 'validating'
        VALIDATING_FAILED = 'validating_failed'
        APPLIED = 'applied'
        APPLY_FAILED = 'apply_failed'


class ProjectConfigVersionSummary:
    """
    The project configuration version.

    :attr str state: The state of the configuration.
    :attr int version: The version number of the configuration.
    :attr str href: A URL.
    """

    def __init__(
        self,
        state: str,
        version: int,
        href: str,
    ) -> None:
        """
        Initialize a ProjectConfigVersionSummary object.

        :param str state: The state of the configuration.
        :param int version: The version number of the configuration.
        :param str href: A URL.
        """
        self.state = state
        self.version = version
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigVersionSummary':
        """Initialize a ProjectConfigVersionSummary object from a json dictionary."""
        args = {}
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectConfigVersionSummary JSON')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in ProjectConfigVersionSummary JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ProjectConfigVersionSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigVersionSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigVersionSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigVersionSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigVersionSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of the configuration.
        """

        APPROVED = 'approved'
        DELETED = 'deleted'
        DELETING = 'deleting'
        DELETING_FAILED = 'deleting_failed'
        DISCARDED = 'discarded'
        DRAFT = 'draft'
        DEPLOYED = 'deployed'
        DEPLOYING_FAILED = 'deploying_failed'
        DEPLOYING = 'deploying'
        SUPERSEDED = 'superseded'
        UNDEPLOYING = 'undeploying'
        UNDEPLOYING_FAILED = 'undeploying_failed'
        VALIDATED = 'validated'
        VALIDATING = 'validating'
        VALIDATING_FAILED = 'validating_failed'
        APPLIED = 'applied'
        APPLY_FAILED = 'apply_failed'


class ProjectConfigVersionSummaryCollection:
    """
    The project configuration version list.

    :attr List[ProjectConfigVersionSummary] versions: The collection list operation
          response schema that defines the array property with the name `versions`.
    """

    def __init__(
        self,
        versions: List['ProjectConfigVersionSummary'],
    ) -> None:
        """
        Initialize a ProjectConfigVersionSummaryCollection object.

        :param List[ProjectConfigVersionSummary] versions: The collection list
               operation response schema that defines the array property with the name
               `versions`.
        """
        self.versions = versions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigVersionSummaryCollection':
        """Initialize a ProjectConfigVersionSummaryCollection object from a json dictionary."""
        args = {}
        if 'versions' in _dict:
            args['versions'] = [ProjectConfigVersionSummary.from_dict(v) for v in _dict.get('versions')]
        else:
            raise ValueError('Required property \'versions\' not present in ProjectConfigVersionSummaryCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigVersionSummaryCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'versions') and self.versions is not None:
            versions_list = []
            for v in self.versions:
                if isinstance(v, dict):
                    versions_list.append(v)
                else:
                    versions_list.append(v.to_dict())
            _dict['versions'] = versions_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigVersionSummaryCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigVersionSummaryCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigVersionSummaryCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectDefinitionProperties:
    """
    The definition of the project.

    :attr str name: The name of the project.  It is unique within the account across
          regions.
    :attr str description: (optional) A brief explanation of the project's use in
          the configuration of a deployable architecture. It is possible to create a
          project without providing a description.
    :attr bool destroy_on_delete: The policy that indicates whether the resources
          are destroyed or not when a project is deleted.
    """

    def __init__(
        self,
        name: str,
        destroy_on_delete: bool,
        *,
        description: str = None,
    ) -> None:
        """
        Initialize a ProjectDefinitionProperties object.

        :param str name: The name of the project.  It is unique within the account
               across regions.
        :param bool destroy_on_delete: The policy that indicates whether the
               resources are destroyed or not when a project is deleted.
        :param str description: (optional) A brief explanation of the project's use
               in the configuration of a deployable architecture. It is possible to create
               a project without providing a description.
        """
        self.name = name
        self.description = description
        self.destroy_on_delete = destroy_on_delete

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectDefinitionProperties':
        """Initialize a ProjectDefinitionProperties object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ProjectDefinitionProperties JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'destroy_on_delete' in _dict:
            args['destroy_on_delete'] = _dict.get('destroy_on_delete')
        else:
            raise ValueError('Required property \'destroy_on_delete\' not present in ProjectDefinitionProperties JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectDefinitionProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'destroy_on_delete') and self.destroy_on_delete is not None:
            _dict['destroy_on_delete'] = self.destroy_on_delete
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectDefinitionProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectDefinitionProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectDefinitionProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectDefinitionReference:
    """
    The definition of the project reference.

    :attr str name: The name of the project.
    """

    def __init__(
        self,
        name: str,
    ) -> None:
        """
        Initialize a ProjectDefinitionReference object.

        :param str name: The name of the project.
        """
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectDefinitionReference':
        """Initialize a ProjectDefinitionReference object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ProjectDefinitionReference JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectDefinitionReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectDefinitionReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectDefinitionReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectDefinitionReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectEnvironmentSummary:
    """
    The environment metadata.

    :attr str id: The environment id as a friendly name.
    :attr ProjectReference project: The project referenced by this resource.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr str href: A URL.
    :attr EnvironmentDefinitionNameDescription definition: The environment
          definition used in the project collection.
    """

    def __init__(
        self,
        id: str,
        project: 'ProjectReference',
        created_at: datetime,
        href: str,
        definition: 'EnvironmentDefinitionNameDescription',
    ) -> None:
        """
        Initialize a ProjectEnvironmentSummary object.

        :param str id: The environment id as a friendly name.
        :param ProjectReference project: The project referenced by this resource.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param str href: A URL.
        :param EnvironmentDefinitionNameDescription definition: The environment
               definition used in the project collection.
        """
        self.id = id
        self.project = project
        self.created_at = created_at
        self.href = href
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectEnvironmentSummary':
        """Initialize a ProjectEnvironmentSummary object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectEnvironmentSummary JSON')
        if 'project' in _dict:
            args['project'] = ProjectReference.from_dict(_dict.get('project'))
        else:
            raise ValueError('Required property \'project\' not present in ProjectEnvironmentSummary JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProjectEnvironmentSummary JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ProjectEnvironmentSummary JSON')
        if 'definition' in _dict:
            args['definition'] = EnvironmentDefinitionNameDescription.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in ProjectEnvironmentSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectEnvironmentSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'project') and self.project is not None:
            if isinstance(self.project, dict):
                _dict['project'] = self.project
            else:
                _dict['project'] = self.project.to_dict()
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectEnvironmentSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectEnvironmentSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectEnvironmentSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectPatchDefinitionBlock:
    """
    The definition of the project.

    :attr str name: (optional) The name of the project.  It is unique within the
          account across regions.
    :attr str description: (optional) A brief explanation of the project's use in
          the configuration of a deployable architecture. It is possible to create a
          project without providing a description.
    :attr bool destroy_on_delete: (optional) The policy that indicates whether the
          resources are destroyed or not when a project is deleted.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
        destroy_on_delete: bool = None,
    ) -> None:
        """
        Initialize a ProjectPatchDefinitionBlock object.

        :param str name: (optional) The name of the project.  It is unique within
               the account across regions.
        :param str description: (optional) A brief explanation of the project's use
               in the configuration of a deployable architecture. It is possible to create
               a project without providing a description.
        :param bool destroy_on_delete: (optional) The policy that indicates whether
               the resources are destroyed or not when a project is deleted.
        """
        self.name = name
        self.description = description
        self.destroy_on_delete = destroy_on_delete

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectPatchDefinitionBlock':
        """Initialize a ProjectPatchDefinitionBlock object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'destroy_on_delete' in _dict:
            args['destroy_on_delete'] = _dict.get('destroy_on_delete')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectPatchDefinitionBlock object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'destroy_on_delete') and self.destroy_on_delete is not None:
            _dict['destroy_on_delete'] = self.destroy_on_delete
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectPatchDefinitionBlock object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectPatchDefinitionBlock') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectPatchDefinitionBlock') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectPrototypeDefinition:
    """
    The definition of the project.

    :attr str name: The name of the project.  It is unique within the account across
          regions.
    :attr str description: (optional) A brief explanation of the project's use in
          the configuration of a deployable architecture. It is possible to create a
          project without providing a description.
    :attr bool destroy_on_delete: (optional) The policy that indicates whether the
          resources are undeployed or not when a project is deleted.
    """

    def __init__(
        self,
        name: str,
        *,
        description: str = None,
        destroy_on_delete: bool = None,
    ) -> None:
        """
        Initialize a ProjectPrototypeDefinition object.

        :param str name: The name of the project.  It is unique within the account
               across regions.
        :param str description: (optional) A brief explanation of the project's use
               in the configuration of a deployable architecture. It is possible to create
               a project without providing a description.
        :param bool destroy_on_delete: (optional) The policy that indicates whether
               the resources are undeployed or not when a project is deleted.
        """
        self.name = name
        self.description = description
        self.destroy_on_delete = destroy_on_delete

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectPrototypeDefinition':
        """Initialize a ProjectPrototypeDefinition object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ProjectPrototypeDefinition JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'destroy_on_delete' in _dict:
            args['destroy_on_delete'] = _dict.get('destroy_on_delete')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectPrototypeDefinition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'destroy_on_delete') and self.destroy_on_delete is not None:
            _dict['destroy_on_delete'] = self.destroy_on_delete
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectPrototypeDefinition object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectPrototypeDefinition') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectPrototypeDefinition') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectReference:
    """
    The project referenced by this resource.

    :attr str id: The unique ID.
    :attr ProjectDefinitionReference definition: The definition of the project
          reference.
    :attr str crn: An IBM Cloud resource name, which uniquely identifies a resource.
    :attr str href: A URL.
    """

    def __init__(
        self,
        id: str,
        definition: 'ProjectDefinitionReference',
        crn: str,
        href: str,
    ) -> None:
        """
        Initialize a ProjectReference object.

        :param str id: The unique ID.
        :param ProjectDefinitionReference definition: The definition of the project
               reference.
        :param str crn: An IBM Cloud resource name, which uniquely identifies a
               resource.
        :param str href: A URL.
        """
        self.id = id
        self.definition = definition
        self.crn = crn
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectReference':
        """Initialize a ProjectReference object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectReference JSON')
        if 'definition' in _dict:
            args['definition'] = ProjectDefinitionReference.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in ProjectReference JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ProjectReference JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ProjectReference JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectSummary:
    """
    ProjectSummary.

    :attr str crn: An IBM Cloud resource name, which uniquely identifies a resource.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr List[CumulativeNeedsAttention] cumulative_needs_attention_view: The
          cumulative list of needs attention items for a project. If the view is
          successfully retrieved, an array which could be empty is returned.
    :attr bool cumulative_needs_attention_view_error: (optional) True indicates that
          the fetch of the needs attention items failed. It only exists if there was an
          error while retrieving the cumulative needs attention view.
    :attr str id: The unique project ID.
    :attr str location: The IBM Cloud location where a resource is deployed.
    :attr str resource_group_id: The resource group id where the project's data and
          tools are created.
    :attr str state: The project status value.
    :attr str href: A URL.
    :attr ProjectDefinitionProperties definition: The definition of the project.
    """

    def __init__(
        self,
        crn: str,
        created_at: datetime,
        cumulative_needs_attention_view: List['CumulativeNeedsAttention'],
        id: str,
        location: str,
        resource_group_id: str,
        state: str,
        href: str,
        definition: 'ProjectDefinitionProperties',
        *,
        cumulative_needs_attention_view_error: bool = None,
    ) -> None:
        """
        Initialize a ProjectSummary object.

        :param str crn: An IBM Cloud resource name, which uniquely identifies a
               resource.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param List[CumulativeNeedsAttention] cumulative_needs_attention_view: The
               cumulative list of needs attention items for a project. If the view is
               successfully retrieved, an array which could be empty is returned.
        :param str id: The unique project ID.
        :param str location: The IBM Cloud location where a resource is deployed.
        :param str resource_group_id: The resource group id where the project's
               data and tools are created.
        :param str state: The project status value.
        :param str href: A URL.
        :param ProjectDefinitionProperties definition: The definition of the
               project.
        :param bool cumulative_needs_attention_view_error: (optional) True
               indicates that the fetch of the needs attention items failed. It only
               exists if there was an error while retrieving the cumulative needs
               attention view.
        """
        self.crn = crn
        self.created_at = created_at
        self.cumulative_needs_attention_view = cumulative_needs_attention_view
        self.cumulative_needs_attention_view_error = cumulative_needs_attention_view_error
        self.id = id
        self.location = location
        self.resource_group_id = resource_group_id
        self.state = state
        self.href = href
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectSummary':
        """Initialize a ProjectSummary object from a json dictionary."""
        args = {}
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ProjectSummary JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProjectSummary JSON')
        if 'cumulative_needs_attention_view' in _dict:
            args['cumulative_needs_attention_view'] = [
                CumulativeNeedsAttention.from_dict(v) for v in _dict.get('cumulative_needs_attention_view')
            ]
        else:
            raise ValueError('Required property \'cumulative_needs_attention_view\' not present in ProjectSummary JSON')
        if 'cumulative_needs_attention_view_error' in _dict:
            args['cumulative_needs_attention_view_error'] = _dict.get('cumulative_needs_attention_view_error')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectSummary JSON')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        else:
            raise ValueError('Required property \'location\' not present in ProjectSummary JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ProjectSummary JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectSummary JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ProjectSummary JSON')
        if 'definition' in _dict:
            args['definition'] = ProjectDefinitionProperties.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in ProjectSummary JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'cumulative_needs_attention_view') and self.cumulative_needs_attention_view is not None:
            cumulative_needs_attention_view_list = []
            for v in self.cumulative_needs_attention_view:
                if isinstance(v, dict):
                    cumulative_needs_attention_view_list.append(v)
                else:
                    cumulative_needs_attention_view_list.append(v.to_dict())
            _dict['cumulative_needs_attention_view'] = cumulative_needs_attention_view_list
        if (
            hasattr(self, 'cumulative_needs_attention_view_error')
            and self.cumulative_needs_attention_view_error is not None
        ):
            _dict['cumulative_needs_attention_view_error'] = self.cumulative_needs_attention_view_error
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The project status value.
        """

        READY = 'ready'
        DELETING = 'deleting'
        DELETING_FAILED = 'deleting_failed'


class SchematicsMetadata:
    """
    A schematics workspace associated to a project configuration, with scripts.

    :attr str workspace_crn: (optional) An IBM Cloud resource name, which uniquely
          identifies a resource.
    :attr Script validate_pre_script: (optional) A script to be run as part of a
          Project configuration, for a given stage (pre, post) and action (validate,
          deploy, undeploy).
    :attr Script validate_post_script: (optional) A script to be run as part of a
          Project configuration, for a given stage (pre, post) and action (validate,
          deploy, undeploy).
    :attr Script deploy_pre_script: (optional) A script to be run as part of a
          Project configuration, for a given stage (pre, post) and action (validate,
          deploy, undeploy).
    :attr Script deploy_post_script: (optional) A script to be run as part of a
          Project configuration, for a given stage (pre, post) and action (validate,
          deploy, undeploy).
    :attr Script undeploy_pre_script: (optional) A script to be run as part of a
          Project configuration, for a given stage (pre, post) and action (validate,
          deploy, undeploy).
    :attr Script undeploy_post_script: (optional) A script to be run as part of a
          Project configuration, for a given stage (pre, post) and action (validate,
          deploy, undeploy).
    """

    def __init__(
        self,
        *,
        workspace_crn: str = None,
        validate_pre_script: 'Script' = None,
        validate_post_script: 'Script' = None,
        deploy_pre_script: 'Script' = None,
        deploy_post_script: 'Script' = None,
        undeploy_pre_script: 'Script' = None,
        undeploy_post_script: 'Script' = None,
    ) -> None:
        """
        Initialize a SchematicsMetadata object.

        :param str workspace_crn: (optional) An IBM Cloud resource name, which
               uniquely identifies a resource.
        :param Script validate_pre_script: (optional) A script to be run as part of
               a Project configuration, for a given stage (pre, post) and action
               (validate, deploy, undeploy).
        :param Script validate_post_script: (optional) A script to be run as part
               of a Project configuration, for a given stage (pre, post) and action
               (validate, deploy, undeploy).
        :param Script deploy_pre_script: (optional) A script to be run as part of a
               Project configuration, for a given stage (pre, post) and action (validate,
               deploy, undeploy).
        :param Script deploy_post_script: (optional) A script to be run as part of
               a Project configuration, for a given stage (pre, post) and action
               (validate, deploy, undeploy).
        :param Script undeploy_pre_script: (optional) A script to be run as part of
               a Project configuration, for a given stage (pre, post) and action
               (validate, deploy, undeploy).
        :param Script undeploy_post_script: (optional) A script to be run as part
               of a Project configuration, for a given stage (pre, post) and action
               (validate, deploy, undeploy).
        """
        self.workspace_crn = workspace_crn
        self.validate_pre_script = validate_pre_script
        self.validate_post_script = validate_post_script
        self.deploy_pre_script = deploy_pre_script
        self.deploy_post_script = deploy_post_script
        self.undeploy_pre_script = undeploy_pre_script
        self.undeploy_post_script = undeploy_post_script

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchematicsMetadata':
        """Initialize a SchematicsMetadata object from a json dictionary."""
        args = {}
        if 'workspace_crn' in _dict:
            args['workspace_crn'] = _dict.get('workspace_crn')
        if 'validate_pre_script' in _dict:
            args['validate_pre_script'] = Script.from_dict(_dict.get('validate_pre_script'))
        if 'validate_post_script' in _dict:
            args['validate_post_script'] = Script.from_dict(_dict.get('validate_post_script'))
        if 'deploy_pre_script' in _dict:
            args['deploy_pre_script'] = Script.from_dict(_dict.get('deploy_pre_script'))
        if 'deploy_post_script' in _dict:
            args['deploy_post_script'] = Script.from_dict(_dict.get('deploy_post_script'))
        if 'undeploy_pre_script' in _dict:
            args['undeploy_pre_script'] = Script.from_dict(_dict.get('undeploy_pre_script'))
        if 'undeploy_post_script' in _dict:
            args['undeploy_post_script'] = Script.from_dict(_dict.get('undeploy_post_script'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchematicsMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'workspace_crn') and self.workspace_crn is not None:
            _dict['workspace_crn'] = self.workspace_crn
        if hasattr(self, 'validate_pre_script') and self.validate_pre_script is not None:
            if isinstance(self.validate_pre_script, dict):
                _dict['validate_pre_script'] = self.validate_pre_script
            else:
                _dict['validate_pre_script'] = self.validate_pre_script.to_dict()
        if hasattr(self, 'validate_post_script') and self.validate_post_script is not None:
            if isinstance(self.validate_post_script, dict):
                _dict['validate_post_script'] = self.validate_post_script
            else:
                _dict['validate_post_script'] = self.validate_post_script.to_dict()
        if hasattr(self, 'deploy_pre_script') and self.deploy_pre_script is not None:
            if isinstance(self.deploy_pre_script, dict):
                _dict['deploy_pre_script'] = self.deploy_pre_script
            else:
                _dict['deploy_pre_script'] = self.deploy_pre_script.to_dict()
        if hasattr(self, 'deploy_post_script') and self.deploy_post_script is not None:
            if isinstance(self.deploy_post_script, dict):
                _dict['deploy_post_script'] = self.deploy_post_script
            else:
                _dict['deploy_post_script'] = self.deploy_post_script.to_dict()
        if hasattr(self, 'undeploy_pre_script') and self.undeploy_pre_script is not None:
            if isinstance(self.undeploy_pre_script, dict):
                _dict['undeploy_pre_script'] = self.undeploy_pre_script
            else:
                _dict['undeploy_pre_script'] = self.undeploy_pre_script.to_dict()
        if hasattr(self, 'undeploy_post_script') and self.undeploy_post_script is not None:
            if isinstance(self.undeploy_post_script, dict):
                _dict['undeploy_post_script'] = self.undeploy_post_script
            else:
                _dict['undeploy_post_script'] = self.undeploy_post_script.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchematicsMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchematicsMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchematicsMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SchematicsWorkspace:
    """
    A Schematics workspace to use for deploying this configuration. Either
    schematics.workspace_crn, definition.locator_id, or both must be specified.

    :attr str workspace_crn: (optional) An IBM Cloud resource name, which uniquely
          identifies a resource.
    """

    def __init__(
        self,
        *,
        workspace_crn: str = None,
    ) -> None:
        """
        Initialize a SchematicsWorkspace object.

        :param str workspace_crn: (optional) An IBM Cloud resource name, which
               uniquely identifies a resource.
        """
        self.workspace_crn = workspace_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchematicsWorkspace':
        """Initialize a SchematicsWorkspace object from a json dictionary."""
        args = {}
        if 'workspace_crn' in _dict:
            args['workspace_crn'] = _dict.get('workspace_crn')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchematicsWorkspace object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'workspace_crn') and self.workspace_crn is not None:
            _dict['workspace_crn'] = self.workspace_crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchematicsWorkspace object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchematicsWorkspace') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchematicsWorkspace') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Script:
    """
    A script to be run as part of a Project configuration, for a given stage (pre, post)
    and action (validate, deploy, undeploy).

    :attr str type: (optional) The type of the script.
    :attr str path: (optional) The path to this script within the current version
          source.
    :attr str short_description: (optional) The short description for this script.
    """

    def __init__(
        self,
        *,
        type: str = None,
        path: str = None,
        short_description: str = None,
    ) -> None:
        """
        Initialize a Script object.

        :param str type: (optional) The type of the script.
        :param str path: (optional) The path to this script within the current
               version source.
        :param str short_description: (optional) The short description for this
               script.
        """
        self.type = type
        self.path = path
        self.short_description = short_description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Script':
        """Initialize a Script object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'short_description' in _dict:
            args['short_description'] = _dict.get('short_description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Script object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'short_description') and self.short_description is not None:
            _dict['short_description'] = self.short_description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Script object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Script') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Script') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TerraformLogAnalyzerErrorMessage:
    """
    The error message parsed by the Terraform Log Analyzer.

    """

    def __init__(
        self,
        **kwargs,
    ) -> None:
        """
        Initialize a TerraformLogAnalyzerErrorMessage object.

        :param **kwargs: (optional) Any additional properties.
        """
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TerraformLogAnalyzerErrorMessage':
        """Initialize a TerraformLogAnalyzerErrorMessage object from a json dictionary."""
        return cls(**_dict)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TerraformLogAnalyzerErrorMessage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        return vars(self)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of TerraformLogAnalyzerErrorMessage"""
        _dict = {}

        for _key in [k for k in vars(self).keys()]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of TerraformLogAnalyzerErrorMessage"""
        for _key in [k for k in vars(self).keys()]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            setattr(self, _key, _value)

    def __str__(self) -> str:
        """Return a `str` version of this TerraformLogAnalyzerErrorMessage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TerraformLogAnalyzerErrorMessage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TerraformLogAnalyzerErrorMessage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TerraformLogAnalyzerSuccessMessage:
    """
    The success message parsed by the Terraform Log Analyzer.

    :attr str resource_type: (optional) The resource type.
    :attr str time_taken: (optional) The time taken.
    :attr str id: (optional) The id.
    """

    def __init__(
        self,
        *,
        resource_type: str = None,
        time_taken: str = None,
        id: str = None,
    ) -> None:
        """
        Initialize a TerraformLogAnalyzerSuccessMessage object.

        :param str resource_type: (optional) The resource type.
        :param str time_taken: (optional) The time taken.
        :param str id: (optional) The id.
        """
        self.resource_type = resource_type
        self.time_taken = time_taken
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TerraformLogAnalyzerSuccessMessage':
        """Initialize a TerraformLogAnalyzerSuccessMessage object from a json dictionary."""
        args = {}
        if 'resource_type' in _dict:
            args['resource_type'] = _dict.get('resource_type')
        if 'time-taken' in _dict:
            args['time_taken'] = _dict.get('time-taken')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TerraformLogAnalyzerSuccessMessage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_type') and self.resource_type is not None:
            _dict['resource_type'] = self.resource_type
        if hasattr(self, 'time_taken') and self.time_taken is not None:
            _dict['time-taken'] = self.time_taken
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TerraformLogAnalyzerSuccessMessage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TerraformLogAnalyzerSuccessMessage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TerraformLogAnalyzerSuccessMessage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigPatchDefinitionBlockDAConfigDefinitionProperties(ProjectConfigPatchDefinitionBlock):
    """
    The name and description of a project configuration.

    :attr str name: (optional) The configuration name. It is unique within the
          account across projects and regions.
    :attr str description: (optional) A project configuration description.
    :attr str environment_id: (optional) The ID of the project environment.
    :attr ProjectConfigAuth authorizations: (optional) The authorization details.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr dict inputs: (optional) The input variables for configuration definition
          and environment.
    :attr dict settings: (optional) Schematics environment variables to use to
          deploy the configuration. Settings are only available if they were specified
          when the configuration was initially created.
    :attr ProjectComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    :attr str locator_id: (optional) A unique concatenation of catalogID.versionID
          that identifies the DA in the catalog. Either schematics.workspace_crn,
          definition.locator_id, or both must be specified.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
        environment_id: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        inputs: dict = None,
        settings: dict = None,
        compliance_profile: 'ProjectComplianceProfile' = None,
        locator_id: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigPatchDefinitionBlockDAConfigDefinitionProperties object.

        :param str name: (optional) The configuration name. It is unique within the
               account across projects and regions.
        :param str description: (optional) A project configuration description.
        :param str environment_id: (optional) The ID of the project environment.
        :param ProjectConfigAuth authorizations: (optional) The authorization
               details. You can authorize by using a trusted profile or an API key in
               Secrets Manager.
        :param dict inputs: (optional) The input variables for configuration
               definition and environment.
        :param dict settings: (optional) Schematics environment variables to use to
               deploy the configuration. Settings are only available if they were
               specified when the configuration was initially created.
        :param ProjectComplianceProfile compliance_profile: (optional) The profile
               required for compliance.
        :param str locator_id: (optional) A unique concatenation of
               catalogID.versionID that identifies the DA in the catalog. Either
               schematics.workspace_crn, definition.locator_id, or both must be specified.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.description = description
        self.environment_id = environment_id
        self.authorizations = authorizations
        self.inputs = inputs
        self.settings = settings
        self.compliance_profile = compliance_profile
        self.locator_id = locator_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigPatchDefinitionBlockDAConfigDefinitionProperties':
        """Initialize a ProjectConfigPatchDefinitionBlockDAConfigDefinitionProperties object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'inputs' in _dict:
            args['inputs'] = _dict.get('inputs')
        if 'settings' in _dict:
            args['settings'] = _dict.get('settings')
        if 'compliance_profile' in _dict:
            args['compliance_profile'] = ProjectComplianceProfile.from_dict(_dict.get('compliance_profile'))
        if 'locator_id' in _dict:
            args['locator_id'] = _dict.get('locator_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigPatchDefinitionBlockDAConfigDefinitionProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'authorizations') and self.authorizations is not None:
            if isinstance(self.authorizations, dict):
                _dict['authorizations'] = self.authorizations
            else:
                _dict['authorizations'] = self.authorizations.to_dict()
        if hasattr(self, 'inputs') and self.inputs is not None:
            _dict['inputs'] = self.inputs
        if hasattr(self, 'settings') and self.settings is not None:
            _dict['settings'] = self.settings
        if hasattr(self, 'compliance_profile') and self.compliance_profile is not None:
            if isinstance(self.compliance_profile, dict):
                _dict['compliance_profile'] = self.compliance_profile
            else:
                _dict['compliance_profile'] = self.compliance_profile.to_dict()
        if hasattr(self, 'locator_id') and self.locator_id is not None:
            _dict['locator_id'] = self.locator_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigPatchDefinitionBlockDAConfigDefinitionProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigPatchDefinitionBlockDAConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigPatchDefinitionBlockDAConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigPatchDefinitionBlockResourceConfigDefinitionProperties(ProjectConfigPatchDefinitionBlock):
    """
    The name and description of a project configuration.

    :attr str name: (optional) The configuration name. It is unique within the
          account across projects and regions.
    :attr str description: (optional) A project configuration description.
    :attr str environment_id: (optional) The ID of the project environment.
    :attr ProjectConfigAuth authorizations: (optional) The authorization details.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr dict inputs: (optional) The input variables for configuration definition
          and environment.
    :attr dict settings: (optional) Schematics environment variables to use to
          deploy the configuration. Settings are only available if they were specified
          when the configuration was initially created.
    :attr List[str] resource_crns: (optional) The CRNs of resources associated with
          this configuration.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
        environment_id: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        inputs: dict = None,
        settings: dict = None,
        resource_crns: List[str] = None,
    ) -> None:
        """
        Initialize a ProjectConfigPatchDefinitionBlockResourceConfigDefinitionProperties object.

        :param str name: (optional) The configuration name. It is unique within the
               account across projects and regions.
        :param str description: (optional) A project configuration description.
        :param str environment_id: (optional) The ID of the project environment.
        :param ProjectConfigAuth authorizations: (optional) The authorization
               details. You can authorize by using a trusted profile or an API key in
               Secrets Manager.
        :param dict inputs: (optional) The input variables for configuration
               definition and environment.
        :param dict settings: (optional) Schematics environment variables to use to
               deploy the configuration. Settings are only available if they were
               specified when the configuration was initially created.
        :param List[str] resource_crns: (optional) The CRNs of resources associated
               with this configuration.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.description = description
        self.environment_id = environment_id
        self.authorizations = authorizations
        self.inputs = inputs
        self.settings = settings
        self.resource_crns = resource_crns

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigPatchDefinitionBlockResourceConfigDefinitionProperties':
        """Initialize a ProjectConfigPatchDefinitionBlockResourceConfigDefinitionProperties object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'inputs' in _dict:
            args['inputs'] = _dict.get('inputs')
        if 'settings' in _dict:
            args['settings'] = _dict.get('settings')
        if 'resource_crns' in _dict:
            args['resource_crns'] = _dict.get('resource_crns')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigPatchDefinitionBlockResourceConfigDefinitionProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'authorizations') and self.authorizations is not None:
            if isinstance(self.authorizations, dict):
                _dict['authorizations'] = self.authorizations
            else:
                _dict['authorizations'] = self.authorizations.to_dict()
        if hasattr(self, 'inputs') and self.inputs is not None:
            _dict['inputs'] = self.inputs
        if hasattr(self, 'settings') and self.settings is not None:
            _dict['settings'] = self.settings
        if hasattr(self, 'resource_crns') and self.resource_crns is not None:
            _dict['resource_crns'] = self.resource_crns
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigPatchDefinitionBlockResourceConfigDefinitionProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigPatchDefinitionBlockResourceConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigPatchDefinitionBlockResourceConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigPrototypeDefinitionBlockDAConfigDefinitionProperties(ProjectConfigPrototypeDefinitionBlock):
    """
    The name and description of a project configuration.

    :attr str name: (optional) The configuration name. It is unique within the
          account across projects and regions.
    :attr str description: (optional) A project configuration description.
    :attr str environment_id: (optional) The ID of the project environment.
    :attr ProjectConfigAuth authorizations: (optional) The authorization details.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr dict inputs: (optional) The input variables for configuration definition
          and environment.
    :attr dict settings: (optional) Schematics environment variables to use to
          deploy the configuration. Settings are only available if they were specified
          when the configuration was initially created.
    :attr ProjectComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    :attr str locator_id: (optional) A unique concatenation of catalogID.versionID
          that identifies the DA in the catalog. Either schematics.workspace_crn,
          definition.locator_id, or both must be specified.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
        environment_id: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        inputs: dict = None,
        settings: dict = None,
        compliance_profile: 'ProjectComplianceProfile' = None,
        locator_id: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigPrototypeDefinitionBlockDAConfigDefinitionProperties object.

        :param str name: (optional) The configuration name. It is unique within the
               account across projects and regions.
        :param str description: (optional) A project configuration description.
        :param str environment_id: (optional) The ID of the project environment.
        :param ProjectConfigAuth authorizations: (optional) The authorization
               details. You can authorize by using a trusted profile or an API key in
               Secrets Manager.
        :param dict inputs: (optional) The input variables for configuration
               definition and environment.
        :param dict settings: (optional) Schematics environment variables to use to
               deploy the configuration. Settings are only available if they were
               specified when the configuration was initially created.
        :param ProjectComplianceProfile compliance_profile: (optional) The profile
               required for compliance.
        :param str locator_id: (optional) A unique concatenation of
               catalogID.versionID that identifies the DA in the catalog. Either
               schematics.workspace_crn, definition.locator_id, or both must be specified.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.description = description
        self.environment_id = environment_id
        self.authorizations = authorizations
        self.inputs = inputs
        self.settings = settings
        self.compliance_profile = compliance_profile
        self.locator_id = locator_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigPrototypeDefinitionBlockDAConfigDefinitionProperties':
        """Initialize a ProjectConfigPrototypeDefinitionBlockDAConfigDefinitionProperties object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'inputs' in _dict:
            args['inputs'] = _dict.get('inputs')
        if 'settings' in _dict:
            args['settings'] = _dict.get('settings')
        if 'compliance_profile' in _dict:
            args['compliance_profile'] = ProjectComplianceProfile.from_dict(_dict.get('compliance_profile'))
        if 'locator_id' in _dict:
            args['locator_id'] = _dict.get('locator_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigPrototypeDefinitionBlockDAConfigDefinitionProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'authorizations') and self.authorizations is not None:
            if isinstance(self.authorizations, dict):
                _dict['authorizations'] = self.authorizations
            else:
                _dict['authorizations'] = self.authorizations.to_dict()
        if hasattr(self, 'inputs') and self.inputs is not None:
            _dict['inputs'] = self.inputs
        if hasattr(self, 'settings') and self.settings is not None:
            _dict['settings'] = self.settings
        if hasattr(self, 'compliance_profile') and self.compliance_profile is not None:
            if isinstance(self.compliance_profile, dict):
                _dict['compliance_profile'] = self.compliance_profile
            else:
                _dict['compliance_profile'] = self.compliance_profile.to_dict()
        if hasattr(self, 'locator_id') and self.locator_id is not None:
            _dict['locator_id'] = self.locator_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigPrototypeDefinitionBlockDAConfigDefinitionProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigPrototypeDefinitionBlockDAConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigPrototypeDefinitionBlockDAConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigPrototypeDefinitionBlockResourceConfigDefinitionProperties(ProjectConfigPrototypeDefinitionBlock):
    """
    The name and description of a project configuration.

    :attr str name: (optional) The configuration name. It is unique within the
          account across projects and regions.
    :attr str description: (optional) A project configuration description.
    :attr str environment_id: (optional) The ID of the project environment.
    :attr ProjectConfigAuth authorizations: (optional) The authorization details.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr dict inputs: (optional) The input variables for configuration definition
          and environment.
    :attr dict settings: (optional) Schematics environment variables to use to
          deploy the configuration. Settings are only available if they were specified
          when the configuration was initially created.
    :attr List[str] resource_crns: (optional) The CRNs of resources associated with
          this configuration.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
        environment_id: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        inputs: dict = None,
        settings: dict = None,
        resource_crns: List[str] = None,
    ) -> None:
        """
        Initialize a ProjectConfigPrototypeDefinitionBlockResourceConfigDefinitionProperties object.

        :param str name: (optional) The configuration name. It is unique within the
               account across projects and regions.
        :param str description: (optional) A project configuration description.
        :param str environment_id: (optional) The ID of the project environment.
        :param ProjectConfigAuth authorizations: (optional) The authorization
               details. You can authorize by using a trusted profile or an API key in
               Secrets Manager.
        :param dict inputs: (optional) The input variables for configuration
               definition and environment.
        :param dict settings: (optional) Schematics environment variables to use to
               deploy the configuration. Settings are only available if they were
               specified when the configuration was initially created.
        :param List[str] resource_crns: (optional) The CRNs of resources associated
               with this configuration.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.description = description
        self.environment_id = environment_id
        self.authorizations = authorizations
        self.inputs = inputs
        self.settings = settings
        self.resource_crns = resource_crns

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigPrototypeDefinitionBlockResourceConfigDefinitionProperties':
        """Initialize a ProjectConfigPrototypeDefinitionBlockResourceConfigDefinitionProperties object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'inputs' in _dict:
            args['inputs'] = _dict.get('inputs')
        if 'settings' in _dict:
            args['settings'] = _dict.get('settings')
        if 'resource_crns' in _dict:
            args['resource_crns'] = _dict.get('resource_crns')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigPrototypeDefinitionBlockResourceConfigDefinitionProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'authorizations') and self.authorizations is not None:
            if isinstance(self.authorizations, dict):
                _dict['authorizations'] = self.authorizations
            else:
                _dict['authorizations'] = self.authorizations.to_dict()
        if hasattr(self, 'inputs') and self.inputs is not None:
            _dict['inputs'] = self.inputs
        if hasattr(self, 'settings') and self.settings is not None:
            _dict['settings'] = self.settings
        if hasattr(self, 'resource_crns') and self.resource_crns is not None:
            _dict['resource_crns'] = self.resource_crns
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigPrototypeDefinitionBlockResourceConfigDefinitionProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigPrototypeDefinitionBlockResourceConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigPrototypeDefinitionBlockResourceConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigResponseDefinitionDAConfigDefinitionProperties(ProjectConfigResponseDefinition):
    """
    The name and description of a project configuration.

    :attr str name: (optional) The configuration name. It is unique within the
          account across projects and regions.
    :attr str description: (optional) A project configuration description.
    :attr str environment_id: (optional) The ID of the project environment.
    :attr ProjectConfigAuth authorizations: (optional) The authorization details.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr dict inputs: (optional) The input variables for configuration definition
          and environment.
    :attr dict settings: (optional) Schematics environment variables to use to
          deploy the configuration. Settings are only available if they were specified
          when the configuration was initially created.
    :attr ProjectComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    :attr str locator_id: (optional) A unique concatenation of catalogID.versionID
          that identifies the DA in the catalog. Either schematics.workspace_crn,
          definition.locator_id, or both must be specified.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
        environment_id: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        inputs: dict = None,
        settings: dict = None,
        compliance_profile: 'ProjectComplianceProfile' = None,
        locator_id: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigResponseDefinitionDAConfigDefinitionProperties object.

        :param str name: (optional) The configuration name. It is unique within the
               account across projects and regions.
        :param str description: (optional) A project configuration description.
        :param str environment_id: (optional) The ID of the project environment.
        :param ProjectConfigAuth authorizations: (optional) The authorization
               details. You can authorize by using a trusted profile or an API key in
               Secrets Manager.
        :param dict inputs: (optional) The input variables for configuration
               definition and environment.
        :param dict settings: (optional) Schematics environment variables to use to
               deploy the configuration. Settings are only available if they were
               specified when the configuration was initially created.
        :param ProjectComplianceProfile compliance_profile: (optional) The profile
               required for compliance.
        :param str locator_id: (optional) A unique concatenation of
               catalogID.versionID that identifies the DA in the catalog. Either
               schematics.workspace_crn, definition.locator_id, or both must be specified.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.description = description
        self.environment_id = environment_id
        self.authorizations = authorizations
        self.inputs = inputs
        self.settings = settings
        self.compliance_profile = compliance_profile
        self.locator_id = locator_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigResponseDefinitionDAConfigDefinitionProperties':
        """Initialize a ProjectConfigResponseDefinitionDAConfigDefinitionProperties object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'inputs' in _dict:
            args['inputs'] = _dict.get('inputs')
        if 'settings' in _dict:
            args['settings'] = _dict.get('settings')
        if 'compliance_profile' in _dict:
            args['compliance_profile'] = ProjectComplianceProfile.from_dict(_dict.get('compliance_profile'))
        if 'locator_id' in _dict:
            args['locator_id'] = _dict.get('locator_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigResponseDefinitionDAConfigDefinitionProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'authorizations') and self.authorizations is not None:
            if isinstance(self.authorizations, dict):
                _dict['authorizations'] = self.authorizations
            else:
                _dict['authorizations'] = self.authorizations.to_dict()
        if hasattr(self, 'inputs') and self.inputs is not None:
            _dict['inputs'] = self.inputs
        if hasattr(self, 'settings') and self.settings is not None:
            _dict['settings'] = self.settings
        if hasattr(self, 'compliance_profile') and self.compliance_profile is not None:
            if isinstance(self.compliance_profile, dict):
                _dict['compliance_profile'] = self.compliance_profile
            else:
                _dict['compliance_profile'] = self.compliance_profile.to_dict()
        if hasattr(self, 'locator_id') and self.locator_id is not None:
            _dict['locator_id'] = self.locator_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigResponseDefinitionDAConfigDefinitionProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigResponseDefinitionDAConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigResponseDefinitionDAConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigResponseDefinitionResourceConfigDefinitionProperties(ProjectConfigResponseDefinition):
    """
    The name and description of a project configuration.

    :attr str name: (optional) The configuration name. It is unique within the
          account across projects and regions.
    :attr str description: (optional) A project configuration description.
    :attr str environment_id: (optional) The ID of the project environment.
    :attr ProjectConfigAuth authorizations: (optional) The authorization details.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr dict inputs: (optional) The input variables for configuration definition
          and environment.
    :attr dict settings: (optional) Schematics environment variables to use to
          deploy the configuration. Settings are only available if they were specified
          when the configuration was initially created.
    :attr List[str] resource_crns: (optional) The CRNs of resources associated with
          this configuration.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
        environment_id: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        inputs: dict = None,
        settings: dict = None,
        resource_crns: List[str] = None,
    ) -> None:
        """
        Initialize a ProjectConfigResponseDefinitionResourceConfigDefinitionProperties object.

        :param str name: (optional) The configuration name. It is unique within the
               account across projects and regions.
        :param str description: (optional) A project configuration description.
        :param str environment_id: (optional) The ID of the project environment.
        :param ProjectConfigAuth authorizations: (optional) The authorization
               details. You can authorize by using a trusted profile or an API key in
               Secrets Manager.
        :param dict inputs: (optional) The input variables for configuration
               definition and environment.
        :param dict settings: (optional) Schematics environment variables to use to
               deploy the configuration. Settings are only available if they were
               specified when the configuration was initially created.
        :param List[str] resource_crns: (optional) The CRNs of resources associated
               with this configuration.
        """
        # pylint: disable=super-init-not-called
        self.name = name
        self.description = description
        self.environment_id = environment_id
        self.authorizations = authorizations
        self.inputs = inputs
        self.settings = settings
        self.resource_crns = resource_crns

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigResponseDefinitionResourceConfigDefinitionProperties':
        """Initialize a ProjectConfigResponseDefinitionResourceConfigDefinitionProperties object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'inputs' in _dict:
            args['inputs'] = _dict.get('inputs')
        if 'settings' in _dict:
            args['settings'] = _dict.get('settings')
        if 'resource_crns' in _dict:
            args['resource_crns'] = _dict.get('resource_crns')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigResponseDefinitionResourceConfigDefinitionProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'environment_id') and self.environment_id is not None:
            _dict['environment_id'] = self.environment_id
        if hasattr(self, 'authorizations') and self.authorizations is not None:
            if isinstance(self.authorizations, dict):
                _dict['authorizations'] = self.authorizations
            else:
                _dict['authorizations'] = self.authorizations.to_dict()
        if hasattr(self, 'inputs') and self.inputs is not None:
            _dict['inputs'] = self.inputs
        if hasattr(self, 'settings') and self.settings is not None:
            _dict['settings'] = self.settings
        if hasattr(self, 'resource_crns') and self.resource_crns is not None:
            _dict['resource_crns'] = self.resource_crns
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigResponseDefinitionResourceConfigDefinitionProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigResponseDefinitionResourceConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigResponseDefinitionResourceConfigDefinitionProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


##############################################################################
# Pagers
##############################################################################


class ProjectsPager:
    """
    ProjectsPager can be used to simplify the use of the "list_projects" method.
    """

    def __init__(
        self,
        *,
        client: ProjectV1,
        limit: int = None,
    ) -> None:
        """
        Initialize a ProjectsPager object.
        :param int limit: (optional) Determine the maximum number of resources to
               return. The number of resources that are returned is the same, with the
               exception of the last page.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of ProjectSummary.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_projects(
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = get_query_param(next_page_link.get('href'), 'start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('projects')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of ProjectSummary.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
