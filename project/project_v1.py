# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.80.0-29334a73-20230925-151553

"""
This document is the **REST API specification** for the Projects Service. The Projects
service provides the capability to manage Infrastructure as Code in IBM Cloud.

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
        service = cls(
            authenticator
            )
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
        :param str resource_group: The resource group where the project's data and
               tools are created.
        :param List[ProjectConfigPrototype] configs: (optional) The project
               configurations. These configurations are only included in the response of
               creating a project if a configs array is specified in the request payload.
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
        definition: 'ProjectPrototypePatchDefinitionBlock',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a project.

        Update a project by the ID.

        :param str id: The unique project ID.
        :param ProjectPrototypePatchDefinitionBlock definition: The definition of
               the project.
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
        all of its artifacts.

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
        :rtype: DetailedResponse with `dict` result representing a `EnvironmentListResponse` object
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
        :param ProjectConfigPrototypeDefinitionBlock definition: The name and
               description of a project configuration.
        :param SchematicsWorkspace schematics: (optional) A schematics workspace
               associated to a project configuration.
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
        definition: 'ProjectConfigPrototypePatchDefinitionBlock',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a configuration.

        Update a configuration in a project by the ID.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param ProjectConfigPrototypePatchDefinitionBlock definition: The name and
               description of a project configuration.
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

        Delete a configuration in a project. Deleting the configuration will also destroy
        all the resources deployed by the configuration if the query parameter `destroy`
        is specified.

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
        *,
        comment: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Force approve project configuration.

        Force approve configuration edits to the main configuration with an approving
        comment.

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
        *,
        x_auth_refresh_token: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Run a validation check.

        Run a validation check on a given configuration in project. The check includes
        creating or updating the associated schematics workspace with a plan job, running
        the CRA scans, and cost estimatation.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param str x_auth_refresh_token: (optional) The IAM refresh token.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigVersion` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {
            'X-Auth-Refresh-Token': x_auth_refresh_token,
        }
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
        Destroy configuration resources.

        Destroy a project's configuration resources. The operation destroys all the
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
        :param SchematicsWorkspace schematics: (optional) A schematics workspace
               associated to a project configuration.
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

        Delete a configuration in a project. Deleting the configuration will also destroy
        all the resources deployed by the configuration if the query parameter `destroy`
        is specified.

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


class ActionJobSummary:
    """
    The summaries of jobs that were performed on the configuration.

    :attr dict plan_summary: (optional) The summary of the plan jobs on the
          configuration.
    :attr dict apply_summary: (optional) The summary of the apply jobs on the
          configuration.
    :attr dict destroy_summary: (optional) The summary of the destroy jobs on the
          configuration.
    :attr dict message_summary: (optional) The message summaries of jobs on the
          configuration.
    :attr dict plan_messages: (optional) The messages of plan jobs on the
          configuration.
    :attr dict apply_messages: (optional) The messages of apply jobs on the
          configuration.
    :attr dict destroy_messages: (optional) The messages of destroy jobs on the
          configuration.
    """

    def __init__(
        self,
        *,
        plan_summary: dict = None,
        apply_summary: dict = None,
        destroy_summary: dict = None,
        message_summary: dict = None,
        plan_messages: dict = None,
        apply_messages: dict = None,
        destroy_messages: dict = None,
    ) -> None:
        """
        Initialize a ActionJobSummary object.

        :param dict plan_summary: (optional) The summary of the plan jobs on the
               configuration.
        :param dict apply_summary: (optional) The summary of the apply jobs on the
               configuration.
        :param dict destroy_summary: (optional) The summary of the destroy jobs on
               the configuration.
        :param dict message_summary: (optional) The message summaries of jobs on
               the configuration.
        :param dict plan_messages: (optional) The messages of plan jobs on the
               configuration.
        :param dict apply_messages: (optional) The messages of apply jobs on the
               configuration.
        :param dict destroy_messages: (optional) The messages of destroy jobs on
               the configuration.
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
            args['plan_summary'] = _dict.get('plan_summary')
        if 'apply_summary' in _dict:
            args['apply_summary'] = _dict.get('apply_summary')
        if 'destroy_summary' in _dict:
            args['destroy_summary'] = _dict.get('destroy_summary')
        if 'message_summary' in _dict:
            args['message_summary'] = _dict.get('message_summary')
        if 'plan_messages' in _dict:
            args['plan_messages'] = _dict.get('plan_messages')
        if 'apply_messages' in _dict:
            args['apply_messages'] = _dict.get('apply_messages')
        if 'destroy_messages' in _dict:
            args['destroy_messages'] = _dict.get('destroy_messages')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionJobSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'plan_summary') and self.plan_summary is not None:
            _dict['plan_summary'] = self.plan_summary
        if hasattr(self, 'apply_summary') and self.apply_summary is not None:
            _dict['apply_summary'] = self.apply_summary
        if hasattr(self, 'destroy_summary') and self.destroy_summary is not None:
            _dict['destroy_summary'] = self.destroy_summary
        if hasattr(self, 'message_summary') and self.message_summary is not None:
            _dict['message_summary'] = self.message_summary
        if hasattr(self, 'plan_messages') and self.plan_messages is not None:
            _dict['plan_messages'] = self.plan_messages
        if hasattr(self, 'apply_messages') and self.apply_messages is not None:
            _dict['apply_messages'] = self.apply_messages
        if hasattr(self, 'destroy_messages') and self.destroy_messages is not None:
            _dict['destroy_messages'] = self.destroy_messages
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

    :attr str id: (optional) The unique ID.
    :attr ActionJobSummary summary: (optional) The summaries of jobs that were
          performed on the configuration.
    """

    def __init__(
        self,
        *,
        id: str = None,
        summary: 'ActionJobSummary' = None,
    ) -> None:
        """
        Initialize a ActionJobWithIdAndSummary object.

        :param str id: (optional) The unique ID.
        :param ActionJobSummary summary: (optional) The summaries of jobs that were
               performed on the configuration.
        """
        self.id = id
        self.summary = summary

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionJobWithIdAndSummary':
        """Initialize a ActionJobWithIdAndSummary object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'summary' in _dict:
            args['summary'] = ActionJobSummary.from_dict(_dict.get('summary'))
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
    :attr str project_id: The unique ID.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr str project_crn: An IBM Cloud resource name, which uniquely identifies a
          resource.
    :attr str target_account: (optional) The target account ID derived from the
          authentication block values.
    :attr datetime user_modified_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr EnvironmentDefinitionRequiredProperties definition: The environment
          definition.
    """

    def __init__(
        self,
        id: str,
        project_id: str,
        created_at: datetime,
        project_crn: str,
        user_modified_at: datetime,
        definition: 'EnvironmentDefinitionRequiredProperties',
        *,
        target_account: str = None,
    ) -> None:
        """
        Initialize a Environment object.

        :param str id: The environment id as a friendly name.
        :param str project_id: The unique ID.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param str project_crn: An IBM Cloud resource name, which uniquely
               identifies a resource.
        :param datetime user_modified_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param EnvironmentDefinitionRequiredProperties definition: The environment
               definition.
        :param str target_account: (optional) The target account ID derived from
               the authentication block values.
        """
        self.id = id
        self.project_id = project_id
        self.created_at = created_at
        self.project_crn = project_crn
        self.target_account = target_account
        self.user_modified_at = user_modified_at
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Environment':
        """Initialize a Environment object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Environment JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in Environment JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in Environment JSON')
        if 'project_crn' in _dict:
            args['project_crn'] = _dict.get('project_crn')
        else:
            raise ValueError('Required property \'project_crn\' not present in Environment JSON')
        if 'target_account' in _dict:
            args['target_account'] = _dict.get('target_account')
        if 'user_modified_at' in _dict:
            args['user_modified_at'] = string_to_datetime(_dict.get('user_modified_at'))
        else:
            raise ValueError('Required property \'user_modified_at\' not present in Environment JSON')
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
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'project_crn') and self.project_crn is not None:
            _dict['project_crn'] = self.project_crn
        if hasattr(self, 'target_account') and self.target_account is not None:
            _dict['target_account'] = self.target_account
        if hasattr(self, 'user_modified_at') and self.user_modified_at is not None:
            _dict['user_modified_at'] = datetime_to_string(self.user_modified_at)
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


class EnvironmentAuth:
    """
    The authorizations for the environment.

    :attr str trusted_profile_id: (optional) The unique ID.
    :attr str method: (optional) The authorization for a configuration. You can
          authorize by using a trusted profile or an API key in Secrets Manager.
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
        Initialize a EnvironmentAuth object.

        :param str trusted_profile_id: (optional) The unique ID.
        :param str method: (optional) The authorization for a configuration. You
               can authorize by using a trusted profile or an API key in Secrets Manager.
        :param str api_key: (optional) The IBM Cloud API Key.
        """
        self.trusted_profile_id = trusted_profile_id
        self.method = method
        self.api_key = api_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentAuth':
        """Initialize a EnvironmentAuth object from a json dictionary."""
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
        """Initialize a EnvironmentAuth object from a json dictionary."""
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
        """Return a `str` version of this EnvironmentAuth object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentAuth') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentAuth') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnvironmentDefinitionNameDescription:
    """
    The environment definition used in the project collection.

    :attr str name: (optional) The name of the environment.
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

        :param str name: (optional) The name of the environment.
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

    :attr str name: (optional) The name of the environment.
    :attr str description: (optional) The description of the environment.
    :attr EnvironmentAuth authorizations: (optional) The authorizations for the
          environment.
    :attr InputVariable inputs: (optional) The input variables for configuration
          definition and environment.
    :attr ProjectComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
        authorizations: 'EnvironmentAuth' = None,
        inputs: 'InputVariable' = None,
        compliance_profile: 'ProjectComplianceProfile' = None,
    ) -> None:
        """
        Initialize a EnvironmentDefinitionProperties object.

        :param str name: (optional) The name of the environment.
        :param str description: (optional) The description of the environment.
        :param EnvironmentAuth authorizations: (optional) The authorizations for
               the environment.
        :param InputVariable inputs: (optional) The input variables for
               configuration definition and environment.
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
            args['authorizations'] = EnvironmentAuth.from_dict(_dict.get('authorizations'))
        if 'inputs' in _dict:
            args['inputs'] = InputVariable.from_dict(_dict.get('inputs'))
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
            if isinstance(self.inputs, dict):
                _dict['inputs'] = self.inputs
            else:
                _dict['inputs'] = self.inputs.to_dict()
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

    :attr str name: The name of the environment.
    :attr str description: (optional) The description of the environment.
    :attr EnvironmentAuth authorizations: (optional) The authorizations for the
          environment.
    :attr InputVariable inputs: (optional) The input variables for configuration
          definition and environment.
    :attr ProjectComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    """

    def __init__(
        self,
        name: str,
        *,
        description: str = None,
        authorizations: 'EnvironmentAuth' = None,
        inputs: 'InputVariable' = None,
        compliance_profile: 'ProjectComplianceProfile' = None,
    ) -> None:
        """
        Initialize a EnvironmentDefinitionRequiredProperties object.

        :param str name: The name of the environment.
        :param str description: (optional) The description of the environment.
        :param EnvironmentAuth authorizations: (optional) The authorizations for
               the environment.
        :param InputVariable inputs: (optional) The input variables for
               configuration definition and environment.
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
            args['authorizations'] = EnvironmentAuth.from_dict(_dict.get('authorizations'))
        if 'inputs' in _dict:
            args['inputs'] = InputVariable.from_dict(_dict.get('inputs'))
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
            if isinstance(self.inputs, dict):
                _dict['inputs'] = self.inputs
            else:
                _dict['inputs'] = self.inputs.to_dict()
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


class EnvironmentListResponse:
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
        Initialize a EnvironmentListResponse object.

        :param List[Environment] environments: (optional) The environments.
        """
        self.environments = environments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentListResponse':
        """Initialize a EnvironmentListResponse object from a json dictionary."""
        args = {}
        if 'environments' in _dict:
            args['environments'] = [Environment.from_dict(v) for v in _dict.get('environments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentListResponse object from a json dictionary."""
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
        """Return a `str` version of this EnvironmentListResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentListResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentListResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class InputVariable:
    """
    The input variables for configuration definition and environment.

    """

    def __init__(
        self,
        **kwargs,
    ) -> None:
        """
        Initialize a InputVariable object.

        :param **kwargs: (optional) Any additional properties.
        """
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InputVariable':
        """Initialize a InputVariable object from a json dictionary."""
        return cls(**_dict)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InputVariable object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        return vars(self)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of InputVariable"""
        _dict = {}

        for _key in [k for k in vars(self).keys()]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of InputVariable"""
        for _key in [k for k in vars(self).keys()]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            setattr(self, _key, _value)

    def __str__(self) -> str:
        """Return a `str` version of this InputVariable object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InputVariable') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InputVariable') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LastActionWithSummary:
    """
    The action job performed on the project configuration.

    :attr str href: (optional) A relative URL.
    :attr str result: (optional) The result of the last action.
    :attr PrePostActionJobWithIdAndSummary pre_job: (optional) A brief summary of a
          pre/post action.
    :attr PrePostActionJobWithIdAndSummary post_job: (optional) A brief summary of a
          pre/post action.
    :attr ActionJobWithIdAndSummary job: (optional) A brief summary of an action.
    """

    def __init__(
        self,
        *,
        href: str = None,
        result: str = None,
        pre_job: 'PrePostActionJobWithIdAndSummary' = None,
        post_job: 'PrePostActionJobWithIdAndSummary' = None,
        job: 'ActionJobWithIdAndSummary' = None,
    ) -> None:
        """
        Initialize a LastActionWithSummary object.

        :param str href: (optional) A relative URL.
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

    :attr str href: (optional) A relative URL.
    :attr str result: (optional) The result of the last action.
    :attr PrePostActionJobWithIdAndSummary pre_job: (optional) A brief summary of a
          pre/post action.
    :attr PrePostActionJobWithIdAndSummary post_job: (optional) A brief summary of a
          pre/post action.
    :attr ActionJobWithIdAndSummary job: (optional) A brief summary of an action.
    :attr ProjectConfigMetadataCostEstimate cost_estimate: (optional) The cost
          estimate of the configuration.
          It only exists after the first configuration validation.
    :attr ProjectConfigMetadataCraLogs cra_logs: (optional) The Code Risk Analyzer
          logs of the configuration.
    """

    def __init__(
        self,
        *,
        href: str = None,
        result: str = None,
        pre_job: 'PrePostActionJobWithIdAndSummary' = None,
        post_job: 'PrePostActionJobWithIdAndSummary' = None,
        job: 'ActionJobWithIdAndSummary' = None,
        cost_estimate: 'ProjectConfigMetadataCostEstimate' = None,
        cra_logs: 'ProjectConfigMetadataCraLogs' = None,
    ) -> None:
        """
        Initialize a LastValidatedActionWithSummary object.

        :param str href: (optional) A relative URL.
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
        :param ProjectConfigMetadataCraLogs cra_logs: (optional) The Code Risk
               Analyzer logs of the configuration.
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
            args['cra_logs'] = ProjectConfigMetadataCraLogs.from_dict(_dict.get('cra_logs'))
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
    :attr object value: (optional) Can be any value - a string, number, boolean,
          array, or object.
    """

    def __init__(
        self,
        name: str,
        *,
        description: str = None,
        value: object = None,
    ) -> None:
        """
        Initialize a OutputValue object.

        :param str name: The variable name.
        :param str description: (optional) A short explanation of the output value.
        :param object value: (optional) Can be any value - a string, number,
               boolean, array, or object.
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

    :attr str href: A relative URL.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a PaginationLink object.

        :param str href: A relative URL.
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


class PrePostActionJobWithIdAndSummary:
    """
    A brief summary of a pre/post action.

    :attr str id: (optional) The unique ID.
    :attr dict summary: (optional) The Summary of the pre/post job of the
          configuration.
    """

    def __init__(
        self,
        *,
        id: str = None,
        summary: dict = None,
    ) -> None:
        """
        Initialize a PrePostActionJobWithIdAndSummary object.

        :param str id: (optional) The unique ID.
        :param dict summary: (optional) The Summary of the pre/post job of the
               configuration.
        """
        self.id = id
        self.summary = summary

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PrePostActionJobWithIdAndSummary':
        """Initialize a PrePostActionJobWithIdAndSummary object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'summary' in _dict:
            args['summary'] = _dict.get('summary')
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
            _dict['summary'] = self.summary
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

    :attr str crn: (optional) An IBM Cloud resource name, which uniquely identifies
          a resource.
    :attr datetime created_at: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr List[CumulativeNeedsAttention] cumulative_needs_attention_view: (optional)
          The cumulative list of needs attention items for a project. If the view is
          successfully retrieved, an array which could be empty is returned.
    :attr bool cumulative_needs_attention_view_error: (optional) True indicates that
          the fetch of the needs attention items failed. It only exists if there was an
          error while retrieving the cumulative needs attention view.
    :attr str id: The unique ID.
    :attr str location: (optional) The IBM Cloud location where a resource is
          deployed.
    :attr str resource_group: (optional) The resource group where the project's data
          and tools are created.
    :attr str state: (optional) The project status value.
    :attr str event_notifications_crn: (optional) The CRN of the event notifications
          instance if one is connected to this project.
    :attr List[ProjectConfigCollectionMember] configs: (optional) The project
          configurations. These configurations are only included in the response of
          creating a project if a configs array is specified in the request payload.
    :attr List[ProjectEnvironmentCollectionMember] environments: (optional) The
          project environments. These environments are only included in the response if
          project environments were created on the project.
    :attr ProjectDefinitionProperties definition: The definition of the project.
    """

    def __init__(
        self,
        id: str,
        definition: 'ProjectDefinitionProperties',
        *,
        crn: str = None,
        created_at: datetime = None,
        cumulative_needs_attention_view: List['CumulativeNeedsAttention'] = None,
        cumulative_needs_attention_view_error: bool = None,
        location: str = None,
        resource_group: str = None,
        state: str = None,
        event_notifications_crn: str = None,
        configs: List['ProjectConfigCollectionMember'] = None,
        environments: List['ProjectEnvironmentCollectionMember'] = None,
    ) -> None:
        """
        Initialize a Project object.

        :param str id: The unique ID.
        :param ProjectDefinitionProperties definition: The definition of the
               project.
        :param str crn: (optional) An IBM Cloud resource name, which uniquely
               identifies a resource.
        :param datetime created_at: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param List[CumulativeNeedsAttention] cumulative_needs_attention_view:
               (optional) The cumulative list of needs attention items for a project. If
               the view is successfully retrieved, an array which could be empty is
               returned.
        :param bool cumulative_needs_attention_view_error: (optional) True
               indicates that the fetch of the needs attention items failed. It only
               exists if there was an error while retrieving the cumulative needs
               attention view.
        :param str location: (optional) The IBM Cloud location where a resource is
               deployed.
        :param str resource_group: (optional) The resource group where the
               project's data and tools are created.
        :param str state: (optional) The project status value.
        :param str event_notifications_crn: (optional) The CRN of the event
               notifications instance if one is connected to this project.
        :param List[ProjectConfigCollectionMember] configs: (optional) The project
               configurations. These configurations are only included in the response of
               creating a project if a configs array is specified in the request payload.
        :param List[ProjectEnvironmentCollectionMember] environments: (optional)
               The project environments. These environments are only included in the
               response if project environments were created on the project.
        """
        self.crn = crn
        self.created_at = created_at
        self.cumulative_needs_attention_view = cumulative_needs_attention_view
        self.cumulative_needs_attention_view_error = cumulative_needs_attention_view_error
        self.id = id
        self.location = location
        self.resource_group = resource_group
        self.state = state
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
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'cumulative_needs_attention_view' in _dict:
            args['cumulative_needs_attention_view'] = [CumulativeNeedsAttention.from_dict(v) for v in _dict.get('cumulative_needs_attention_view')]
        if 'cumulative_needs_attention_view_error' in _dict:
            args['cumulative_needs_attention_view_error'] = _dict.get('cumulative_needs_attention_view_error')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Project JSON')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        if 'resource_group' in _dict:
            args['resource_group'] = _dict.get('resource_group')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'event_notifications_crn' in _dict:
            args['event_notifications_crn'] = _dict.get('event_notifications_crn')
        if 'configs' in _dict:
            args['configs'] = [ProjectConfigCollectionMember.from_dict(v) for v in _dict.get('configs')]
        if 'environments' in _dict:
            args['environments'] = [ProjectEnvironmentCollectionMember.from_dict(v) for v in _dict.get('environments')]
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
        if hasattr(self, 'cumulative_needs_attention_view_error') and self.cumulative_needs_attention_view_error is not None:
            _dict['cumulative_needs_attention_view_error'] = self.cumulative_needs_attention_view_error
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group') and self.resource_group is not None:
            _dict['resource_group'] = self.resource_group
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
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
    :attr int total_count: Get the occurrencies of the total projects.
    :attr PaginationLink first: A pagination link.
    :attr PaginationLink last: (optional) A pagination link.
    :attr PaginationLink previous: (optional) A pagination link.
    :attr PaginationLink next: (optional) A pagination link.
    :attr List[ProjectCollectionMemberWithMetadata] projects: (optional) An array of
          projects.
    """

    def __init__(
        self,
        limit: int,
        total_count: int,
        first: 'PaginationLink',
        *,
        last: 'PaginationLink' = None,
        previous: 'PaginationLink' = None,
        next: 'PaginationLink' = None,
        projects: List['ProjectCollectionMemberWithMetadata'] = None,
    ) -> None:
        """
        Initialize a ProjectCollection object.

        :param int limit: A pagination limit.
        :param int total_count: Get the occurrencies of the total projects.
        :param PaginationLink first: A pagination link.
        :param PaginationLink last: (optional) A pagination link.
        :param PaginationLink previous: (optional) A pagination link.
        :param PaginationLink next: (optional) A pagination link.
        :param List[ProjectCollectionMemberWithMetadata] projects: (optional) An
               array of projects.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.last = last
        self.previous = previous
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
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ProjectCollection JSON')
        if 'first' in _dict:
            args['first'] = PaginationLink.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ProjectCollection JSON')
        if 'last' in _dict:
            args['last'] = PaginationLink.from_dict(_dict.get('last'))
        if 'previous' in _dict:
            args['previous'] = PaginationLink.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = PaginationLink.from_dict(_dict.get('next'))
        if 'projects' in _dict:
            args['projects'] = [ProjectCollectionMemberWithMetadata.from_dict(v) for v in _dict.get('projects')]
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
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            if isinstance(self.last, dict):
                _dict['last'] = self.last
            else:
                _dict['last'] = self.last.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            if isinstance(self.previous, dict):
                _dict['previous'] = self.previous
            else:
                _dict['previous'] = self.previous.to_dict()
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


class ProjectCollectionMemberWithMetadata:
    """
    ProjectCollectionMemberWithMetadata.

    :attr str crn: (optional) An IBM Cloud resource name, which uniquely identifies
          a resource.
    :attr datetime created_at: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr List[CumulativeNeedsAttention] cumulative_needs_attention_view: (optional)
          The cumulative list of needs attention items for a project. If the view is
          successfully retrieved, an array which could be empty is returned.
    :attr bool cumulative_needs_attention_view_error: (optional) True indicates that
          the fetch of the needs attention items failed. It only exists if there was an
          error while retrieving the cumulative needs attention view.
    :attr str id: The unique ID.
    :attr str location: (optional) The IBM Cloud location where a resource is
          deployed.
    :attr str resource_group: (optional) The resource group where the project's data
          and tools are created.
    :attr str state: (optional) The project status value.
    :attr str event_notifications_crn: (optional) The CRN of the event notifications
          instance if one is connected to this project.
    :attr ProjectDefinitionProperties definition: The definition of the project.
    """

    def __init__(
        self,
        id: str,
        definition: 'ProjectDefinitionProperties',
        *,
        crn: str = None,
        created_at: datetime = None,
        cumulative_needs_attention_view: List['CumulativeNeedsAttention'] = None,
        cumulative_needs_attention_view_error: bool = None,
        location: str = None,
        resource_group: str = None,
        state: str = None,
        event_notifications_crn: str = None,
    ) -> None:
        """
        Initialize a ProjectCollectionMemberWithMetadata object.

        :param str id: The unique ID.
        :param ProjectDefinitionProperties definition: The definition of the
               project.
        :param str crn: (optional) An IBM Cloud resource name, which uniquely
               identifies a resource.
        :param datetime created_at: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param List[CumulativeNeedsAttention] cumulative_needs_attention_view:
               (optional) The cumulative list of needs attention items for a project. If
               the view is successfully retrieved, an array which could be empty is
               returned.
        :param bool cumulative_needs_attention_view_error: (optional) True
               indicates that the fetch of the needs attention items failed. It only
               exists if there was an error while retrieving the cumulative needs
               attention view.
        :param str location: (optional) The IBM Cloud location where a resource is
               deployed.
        :param str resource_group: (optional) The resource group where the
               project's data and tools are created.
        :param str state: (optional) The project status value.
        :param str event_notifications_crn: (optional) The CRN of the event
               notifications instance if one is connected to this project.
        """
        self.crn = crn
        self.created_at = created_at
        self.cumulative_needs_attention_view = cumulative_needs_attention_view
        self.cumulative_needs_attention_view_error = cumulative_needs_attention_view_error
        self.id = id
        self.location = location
        self.resource_group = resource_group
        self.state = state
        self.event_notifications_crn = event_notifications_crn
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectCollectionMemberWithMetadata':
        """Initialize a ProjectCollectionMemberWithMetadata object from a json dictionary."""
        args = {}
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'cumulative_needs_attention_view' in _dict:
            args['cumulative_needs_attention_view'] = [CumulativeNeedsAttention.from_dict(v) for v in _dict.get('cumulative_needs_attention_view')]
        if 'cumulative_needs_attention_view_error' in _dict:
            args['cumulative_needs_attention_view_error'] = _dict.get('cumulative_needs_attention_view_error')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectCollectionMemberWithMetadata JSON')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        if 'resource_group' in _dict:
            args['resource_group'] = _dict.get('resource_group')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'event_notifications_crn' in _dict:
            args['event_notifications_crn'] = _dict.get('event_notifications_crn')
        if 'definition' in _dict:
            args['definition'] = ProjectDefinitionProperties.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in ProjectCollectionMemberWithMetadata JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectCollectionMemberWithMetadata object from a json dictionary."""
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
        if hasattr(self, 'cumulative_needs_attention_view_error') and self.cumulative_needs_attention_view_error is not None:
            _dict['cumulative_needs_attention_view_error'] = self.cumulative_needs_attention_view_error
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group') and self.resource_group is not None:
            _dict['resource_group'] = self.resource_group
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'event_notifications_crn') and self.event_notifications_crn is not None:
            _dict['event_notifications_crn'] = self.event_notifications_crn
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
        """Return a `str` version of this ProjectCollectionMemberWithMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectCollectionMemberWithMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectCollectionMemberWithMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The project status value.
        """

        READY = 'ready'
        DELETING = 'deleting'
        DELETING_FAILED = 'deleting_failed'



class ProjectComplianceProfile:
    """
    The profile required for compliance.

    :attr str id: (optional) The unique ID.
    :attr str instance_id: (optional) The unique ID.
    :attr str instance_location: (optional) The location of the compliance instance.
    :attr str attachment_id: (optional) The unique ID.
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

        :param str id: (optional) The unique ID.
        :param str instance_id: (optional) The unique ID.
        :param str instance_location: (optional) The location of the compliance
               instance.
        :param str attachment_id: (optional) The unique ID.
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
    :attr str project_id: The unique ID.
    :attr int version: The version of the configuration.
    :attr bool is_draft: The flag that indicates whether the version of the
          configuration is draft, or active.
    :attr List[object] needs_attention_state: (optional) The needs attention state
          of a configuration.
    :attr str state: The state of the configuration.
    :attr bool update_available: The flag that indicates whether a configuration
          update is available.
    :attr datetime created_at: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr datetime user_modified_at: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr ProjectConfigMetadataLastApproved last_approved: (optional) The last
          approved metadata of the configuration.
    :attr datetime last_save: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr dict references: (optional) The references used in the config to resolve
          input values.
    :attr LastValidatedActionWithSummary last_validated: (optional) The action job
          performed on the project configuration.
    :attr LastActionWithSummary last_deployed: (optional) The action job performed
          on the project configuration.
    :attr LastActionWithSummary last_undeployed: (optional) The action job performed
          on the project configuration.
    :attr SchematicsWorkspace schematics: (optional) A schematics workspace
          associated to a project configuration.
    :attr ProjectConfigResponseDefinition definition: The type and output of a
          project configuration.
    :attr ProjectConfigVersionSummary approved_version: (optional) The project
          configuration version.
    :attr ProjectConfigVersionSummary deployed_version: (optional) The project
          configuration version.
    """

    def __init__(
        self,
        id: str,
        project_id: str,
        version: int,
        is_draft: bool,
        state: str,
        update_available: bool,
        definition: 'ProjectConfigResponseDefinition',
        *,
        needs_attention_state: List[object] = None,
        created_at: datetime = None,
        user_modified_at: datetime = None,
        last_approved: 'ProjectConfigMetadataLastApproved' = None,
        last_save: datetime = None,
        references: dict = None,
        last_validated: 'LastValidatedActionWithSummary' = None,
        last_deployed: 'LastActionWithSummary' = None,
        last_undeployed: 'LastActionWithSummary' = None,
        schematics: 'SchematicsWorkspace' = None,
        approved_version: 'ProjectConfigVersionSummary' = None,
        deployed_version: 'ProjectConfigVersionSummary' = None,
    ) -> None:
        """
        Initialize a ProjectConfig object.

        :param str id: The ID of the configuration. If this parameter is empty, an
               ID is automatically created for the configuration.
        :param str project_id: The unique ID.
        :param int version: The version of the configuration.
        :param bool is_draft: The flag that indicates whether the version of the
               configuration is draft, or active.
        :param str state: The state of the configuration.
        :param bool update_available: The flag that indicates whether a
               configuration update is available.
        :param ProjectConfigResponseDefinition definition: The type and output of a
               project configuration.
        :param List[object] needs_attention_state: (optional) The needs attention
               state of a configuration.
        :param datetime created_at: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param datetime user_modified_at: (optional) A date and time value in the
               format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date
               and time format as specified by RFC 3339.
        :param ProjectConfigMetadataLastApproved last_approved: (optional) The last
               approved metadata of the configuration.
        :param datetime last_save: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param dict references: (optional) The references used in the config to
               resolve input values.
        :param LastValidatedActionWithSummary last_validated: (optional) The action
               job performed on the project configuration.
        :param LastActionWithSummary last_deployed: (optional) The action job
               performed on the project configuration.
        :param LastActionWithSummary last_undeployed: (optional) The action job
               performed on the project configuration.
        :param SchematicsWorkspace schematics: (optional) A schematics workspace
               associated to a project configuration.
        :param ProjectConfigVersionSummary approved_version: (optional) The project
               configuration version.
        :param ProjectConfigVersionSummary deployed_version: (optional) The project
               configuration version.
        """
        self.id = id
        self.project_id = project_id
        self.version = version
        self.is_draft = is_draft
        self.needs_attention_state = needs_attention_state
        self.state = state
        self.update_available = update_available
        self.created_at = created_at
        self.user_modified_at = user_modified_at
        self.last_approved = last_approved
        self.last_save = last_save
        self.references = references
        self.last_validated = last_validated
        self.last_deployed = last_deployed
        self.last_undeployed = last_undeployed
        self.schematics = schematics
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
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in ProjectConfig JSON')
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
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectConfig JSON')
        if 'update_available' in _dict:
            args['update_available'] = _dict.get('update_available')
        else:
            raise ValueError('Required property \'update_available\' not present in ProjectConfig JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'user_modified_at' in _dict:
            args['user_modified_at'] = string_to_datetime(_dict.get('user_modified_at'))
        if 'last_approved' in _dict:
            args['last_approved'] = ProjectConfigMetadataLastApproved.from_dict(_dict.get('last_approved'))
        if 'last_save' in _dict:
            args['last_save'] = string_to_datetime(_dict.get('last_save'))
        if 'references' in _dict:
            args['references'] = _dict.get('references')
        if 'last_validated' in _dict:
            args['last_validated'] = LastValidatedActionWithSummary.from_dict(_dict.get('last_validated'))
        if 'last_deployed' in _dict:
            args['last_deployed'] = LastActionWithSummary.from_dict(_dict.get('last_deployed'))
        if 'last_undeployed' in _dict:
            args['last_undeployed'] = LastActionWithSummary.from_dict(_dict.get('last_undeployed'))
        if 'schematics' in _dict:
            args['schematics'] = SchematicsWorkspace.from_dict(_dict.get('schematics'))
        if 'definition' in _dict:
            args['definition'] = ProjectConfigResponseDefinition.from_dict(_dict.get('definition'))
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
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'is_draft') and self.is_draft is not None:
            _dict['is_draft'] = self.is_draft
        if hasattr(self, 'needs_attention_state') and self.needs_attention_state is not None:
            _dict['needs_attention_state'] = self.needs_attention_state
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'update_available') and self.update_available is not None:
            _dict['update_available'] = self.update_available
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'user_modified_at') and self.user_modified_at is not None:
            _dict['user_modified_at'] = datetime_to_string(self.user_modified_at)
        if hasattr(self, 'last_approved') and self.last_approved is not None:
            if isinstance(self.last_approved, dict):
                _dict['last_approved'] = self.last_approved
            else:
                _dict['last_approved'] = self.last_approved.to_dict()
        if hasattr(self, 'last_save') and self.last_save is not None:
            _dict['last_save'] = datetime_to_string(self.last_save)
        if hasattr(self, 'references') and self.references is not None:
            _dict['references'] = self.references
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
        if hasattr(self, 'schematics') and self.schematics is not None:
            if isinstance(self.schematics, dict):
                _dict['schematics'] = self.schematics
            else:
                _dict['schematics'] = self.schematics.to_dict()
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
        SUPERCEDED = 'superceded'
        UNDEPLOYING = 'undeploying'
        UNDEPLOYING_FAILED = 'undeploying_failed'
        VALIDATED = 'validated'
        VALIDATING = 'validating'
        VALIDATING_FAILED = 'validating_failed'



class ProjectConfigAuth:
    """
    The authorization for a configuration. You can authorize by using a trusted profile or
    an API key in Secrets Manager.

    :attr ProjectConfigAuthTrustedProfile trusted_profile: (optional) The trusted
          profile for authorizations.
    :attr str method: (optional) The authorization for a configuration. You can
          authorize by using a trusted profile or an API key in Secrets Manager.
    :attr str api_key: (optional) The IBM Cloud API Key.
    """

    def __init__(
        self,
        *,
        trusted_profile: 'ProjectConfigAuthTrustedProfile' = None,
        method: str = None,
        api_key: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigAuth object.

        :param ProjectConfigAuthTrustedProfile trusted_profile: (optional) The
               trusted profile for authorizations.
        :param str method: (optional) The authorization for a configuration. You
               can authorize by using a trusted profile or an API key in Secrets Manager.
        :param str api_key: (optional) The IBM Cloud API Key.
        """
        self.trusted_profile = trusted_profile
        self.method = method
        self.api_key = api_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigAuth':
        """Initialize a ProjectConfigAuth object from a json dictionary."""
        args = {}
        if 'trusted_profile' in _dict:
            args['trusted_profile'] = ProjectConfigAuthTrustedProfile.from_dict(_dict.get('trusted_profile'))
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
        if hasattr(self, 'trusted_profile') and self.trusted_profile is not None:
            if isinstance(self.trusted_profile, dict):
                _dict['trusted_profile'] = self.trusted_profile
            else:
                _dict['trusted_profile'] = self.trusted_profile.to_dict()
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


class ProjectConfigAuthTrustedProfile:
    """
    The trusted profile for authorizations.

    :attr str id: (optional) The unique ID.
    :attr str target_iam_id: (optional) The unique ID.
    """

    def __init__(
        self,
        *,
        id: str = None,
        target_iam_id: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigAuthTrustedProfile object.

        :param str id: (optional) The unique ID.
        :param str target_iam_id: (optional) The unique ID.
        """
        self.id = id
        self.target_iam_id = target_iam_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigAuthTrustedProfile':
        """Initialize a ProjectConfigAuthTrustedProfile object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'target_iam_id' in _dict:
            args['target_iam_id'] = _dict.get('target_iam_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigAuthTrustedProfile object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'target_iam_id') and self.target_iam_id is not None:
            _dict['target_iam_id'] = self.target_iam_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigAuthTrustedProfile object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigAuthTrustedProfile') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigAuthTrustedProfile') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigCollection:
    """
    The project configuration list.

    :attr List[ProjectConfigCollectionMember] configs: (optional) The collection
          list operation response schema that should define the array property with the
          name "configs".
    """

    def __init__(
        self,
        *,
        configs: List['ProjectConfigCollectionMember'] = None,
    ) -> None:
        """
        Initialize a ProjectConfigCollection object.

        :param List[ProjectConfigCollectionMember] configs: (optional) The
               collection list operation response schema that should define the array
               property with the name "configs".
        """
        self.configs = configs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigCollection':
        """Initialize a ProjectConfigCollection object from a json dictionary."""
        args = {}
        if 'configs' in _dict:
            args['configs'] = [ProjectConfigCollectionMember.from_dict(v) for v in _dict.get('configs')]
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


class ProjectConfigCollectionMember:
    """
    ProjectConfigCollectionMember.

    :attr ProjectConfigVersionSummary approved_version: (optional) The project
          configuration version.
    :attr ProjectConfigVersionSummary deployed_version: (optional) The project
          configuration version.
    :attr str id: The ID of the configuration. If this parameter is empty, an ID is
          automatically created for the configuration.
    :attr str project_id: The unique ID.
    :attr int version: The version of the configuration.
    :attr bool is_draft: The flag that indicates whether the version of the
          configuration is draft, or active.
    :attr List[object] needs_attention_state: (optional) The needs attention state
          of a configuration.
    :attr str state: The state of the configuration.
    :attr bool update_available: The flag that indicates whether a configuration
          update is available.
    :attr datetime created_at: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr datetime user_modified_at: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr ProjectConfigMetadataLastApproved last_approved: (optional) The last
          approved metadata of the configuration.
    :attr datetime last_save: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr dict references: (optional) The references used in the config to resolve
          input values.
    :attr LastValidatedActionWithSummary last_validated: (optional) The action job
          performed on the project configuration.
    :attr LastActionWithSummary last_deployed: (optional) The action job performed
          on the project configuration.
    :attr LastActionWithSummary last_undeployed: (optional) The action job performed
          on the project configuration.
    :attr SchematicsWorkspace schematics: (optional) A schematics workspace
          associated to a project configuration.
    :attr str href: A relative URL.
    :attr ProjectConfigDefinitionNameDescription definition: The name and
          description of a project configuration.
    """

    def __init__(
        self,
        id: str,
        project_id: str,
        version: int,
        is_draft: bool,
        state: str,
        update_available: bool,
        href: str,
        definition: 'ProjectConfigDefinitionNameDescription',
        *,
        approved_version: 'ProjectConfigVersionSummary' = None,
        deployed_version: 'ProjectConfigVersionSummary' = None,
        needs_attention_state: List[object] = None,
        created_at: datetime = None,
        user_modified_at: datetime = None,
        last_approved: 'ProjectConfigMetadataLastApproved' = None,
        last_save: datetime = None,
        references: dict = None,
        last_validated: 'LastValidatedActionWithSummary' = None,
        last_deployed: 'LastActionWithSummary' = None,
        last_undeployed: 'LastActionWithSummary' = None,
        schematics: 'SchematicsWorkspace' = None,
    ) -> None:
        """
        Initialize a ProjectConfigCollectionMember object.

        :param str id: The ID of the configuration. If this parameter is empty, an
               ID is automatically created for the configuration.
        :param str project_id: The unique ID.
        :param int version: The version of the configuration.
        :param bool is_draft: The flag that indicates whether the version of the
               configuration is draft, or active.
        :param str state: The state of the configuration.
        :param bool update_available: The flag that indicates whether a
               configuration update is available.
        :param str href: A relative URL.
        :param ProjectConfigDefinitionNameDescription definition: The name and
               description of a project configuration.
        :param ProjectConfigVersionSummary approved_version: (optional) The project
               configuration version.
        :param ProjectConfigVersionSummary deployed_version: (optional) The project
               configuration version.
        :param List[object] needs_attention_state: (optional) The needs attention
               state of a configuration.
        :param datetime created_at: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param datetime user_modified_at: (optional) A date and time value in the
               format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date
               and time format as specified by RFC 3339.
        :param ProjectConfigMetadataLastApproved last_approved: (optional) The last
               approved metadata of the configuration.
        :param datetime last_save: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param dict references: (optional) The references used in the config to
               resolve input values.
        :param LastValidatedActionWithSummary last_validated: (optional) The action
               job performed on the project configuration.
        :param LastActionWithSummary last_deployed: (optional) The action job
               performed on the project configuration.
        :param LastActionWithSummary last_undeployed: (optional) The action job
               performed on the project configuration.
        :param SchematicsWorkspace schematics: (optional) A schematics workspace
               associated to a project configuration.
        """
        self.approved_version = approved_version
        self.deployed_version = deployed_version
        self.id = id
        self.project_id = project_id
        self.version = version
        self.is_draft = is_draft
        self.needs_attention_state = needs_attention_state
        self.state = state
        self.update_available = update_available
        self.created_at = created_at
        self.user_modified_at = user_modified_at
        self.last_approved = last_approved
        self.last_save = last_save
        self.references = references
        self.last_validated = last_validated
        self.last_deployed = last_deployed
        self.last_undeployed = last_undeployed
        self.schematics = schematics
        self.href = href
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigCollectionMember':
        """Initialize a ProjectConfigCollectionMember object from a json dictionary."""
        args = {}
        if 'approved_version' in _dict:
            args['approved_version'] = ProjectConfigVersionSummary.from_dict(_dict.get('approved_version'))
        if 'deployed_version' in _dict:
            args['deployed_version'] = ProjectConfigVersionSummary.from_dict(_dict.get('deployed_version'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectConfigCollectionMember JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in ProjectConfigCollectionMember JSON')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in ProjectConfigCollectionMember JSON')
        if 'is_draft' in _dict:
            args['is_draft'] = _dict.get('is_draft')
        else:
            raise ValueError('Required property \'is_draft\' not present in ProjectConfigCollectionMember JSON')
        if 'needs_attention_state' in _dict:
            args['needs_attention_state'] = _dict.get('needs_attention_state')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectConfigCollectionMember JSON')
        if 'update_available' in _dict:
            args['update_available'] = _dict.get('update_available')
        else:
            raise ValueError('Required property \'update_available\' not present in ProjectConfigCollectionMember JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'user_modified_at' in _dict:
            args['user_modified_at'] = string_to_datetime(_dict.get('user_modified_at'))
        if 'last_approved' in _dict:
            args['last_approved'] = ProjectConfigMetadataLastApproved.from_dict(_dict.get('last_approved'))
        if 'last_save' in _dict:
            args['last_save'] = string_to_datetime(_dict.get('last_save'))
        if 'references' in _dict:
            args['references'] = _dict.get('references')
        if 'last_validated' in _dict:
            args['last_validated'] = LastValidatedActionWithSummary.from_dict(_dict.get('last_validated'))
        if 'last_deployed' in _dict:
            args['last_deployed'] = LastActionWithSummary.from_dict(_dict.get('last_deployed'))
        if 'last_undeployed' in _dict:
            args['last_undeployed'] = LastActionWithSummary.from_dict(_dict.get('last_undeployed'))
        if 'schematics' in _dict:
            args['schematics'] = SchematicsWorkspace.from_dict(_dict.get('schematics'))
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ProjectConfigCollectionMember JSON')
        if 'definition' in _dict:
            args['definition'] = ProjectConfigDefinitionNameDescription.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in ProjectConfigCollectionMember JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigCollectionMember object from a json dictionary."""
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
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'is_draft') and self.is_draft is not None:
            _dict['is_draft'] = self.is_draft
        if hasattr(self, 'needs_attention_state') and self.needs_attention_state is not None:
            _dict['needs_attention_state'] = self.needs_attention_state
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'update_available') and self.update_available is not None:
            _dict['update_available'] = self.update_available
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'user_modified_at') and self.user_modified_at is not None:
            _dict['user_modified_at'] = datetime_to_string(self.user_modified_at)
        if hasattr(self, 'last_approved') and self.last_approved is not None:
            if isinstance(self.last_approved, dict):
                _dict['last_approved'] = self.last_approved
            else:
                _dict['last_approved'] = self.last_approved.to_dict()
        if hasattr(self, 'last_save') and self.last_save is not None:
            _dict['last_save'] = datetime_to_string(self.last_save)
        if hasattr(self, 'references') and self.references is not None:
            _dict['references'] = self.references
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
        if hasattr(self, 'schematics') and self.schematics is not None:
            if isinstance(self.schematics, dict):
                _dict['schematics'] = self.schematics
            else:
                _dict['schematics'] = self.schematics.to_dict()
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
        """Return a `str` version of this ProjectConfigCollectionMember object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigCollectionMember') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigCollectionMember') -> bool:
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
        SUPERCEDED = 'superceded'
        UNDEPLOYING = 'undeploying'
        UNDEPLOYING_FAILED = 'undeploying_failed'
        VALIDATED = 'validated'
        VALIDATING = 'validating'
        VALIDATING_FAILED = 'validating_failed'



class ProjectConfigDefinitionNameDescription:
    """
    The name and description of a project configuration.

    :attr str name: (optional) The configuration name.
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

        :param str name: (optional) The configuration name.
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

    :attr str id: The unique ID.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a ProjectConfigDelete object.

        :param str id: The unique ID.
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


class ProjectConfigMetadataCraLogs:
    """
    The Code Risk Analyzer logs of the configuration.

    :attr str cra_version: (optional) The version of the Code Risk Analyzer logs of
          the configuration.
    :attr str schema_version: (optional) The schema version of Code Risk Analyzer
          logs of the configuration.
    :attr str status: (optional) The status of the Code Risk Analyzer logs of the
          configuration.
    :attr dict summary: (optional) The summary of the Code Risk Analyzer logs of the
          configuration.
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
        summary: dict = None,
        timestamp: datetime = None,
    ) -> None:
        """
        Initialize a ProjectConfigMetadataCraLogs object.

        :param str cra_version: (optional) The version of the Code Risk Analyzer
               logs of the configuration.
        :param str schema_version: (optional) The schema version of Code Risk
               Analyzer logs of the configuration.
        :param str status: (optional) The status of the Code Risk Analyzer logs of
               the configuration.
        :param dict summary: (optional) The summary of the Code Risk Analyzer logs
               of the configuration.
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
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigMetadataCraLogs':
        """Initialize a ProjectConfigMetadataCraLogs object from a json dictionary."""
        args = {}
        if 'cra_version' in _dict:
            args['cra_version'] = _dict.get('cra_version')
        if 'schema_version' in _dict:
            args['schema_version'] = _dict.get('schema_version')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'summary' in _dict:
            args['summary'] = _dict.get('summary')
        if 'timestamp' in _dict:
            args['timestamp'] = string_to_datetime(_dict.get('timestamp'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigMetadataCraLogs object from a json dictionary."""
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
            _dict['summary'] = self.summary
        if hasattr(self, 'timestamp') and self.timestamp is not None:
            _dict['timestamp'] = datetime_to_string(self.timestamp)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigMetadataCraLogs object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigMetadataCraLogs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigMetadataCraLogs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigMetadataLastApproved:
    """
    The last approved metadata of the configuration.

    :attr bool is_forced: The flag that indicates whether the approval was forced
          approved.
    :attr str comment: (optional) The comment left by the user who approved the
          configuration.
    :attr datetime timestamp: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr str user_id: The unique ID.
    """

    def __init__(
        self,
        is_forced: bool,
        timestamp: datetime,
        user_id: str,
        *,
        comment: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigMetadataLastApproved object.

        :param bool is_forced: The flag that indicates whether the approval was
               forced approved.
        :param datetime timestamp: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param str user_id: The unique ID.
        :param str comment: (optional) The comment left by the user who approved
               the configuration.
        """
        self.is_forced = is_forced
        self.comment = comment
        self.timestamp = timestamp
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigMetadataLastApproved':
        """Initialize a ProjectConfigMetadataLastApproved object from a json dictionary."""
        args = {}
        if 'is_forced' in _dict:
            args['is_forced'] = _dict.get('is_forced')
        else:
            raise ValueError('Required property \'is_forced\' not present in ProjectConfigMetadataLastApproved JSON')
        if 'comment' in _dict:
            args['comment'] = _dict.get('comment')
        if 'timestamp' in _dict:
            args['timestamp'] = string_to_datetime(_dict.get('timestamp'))
        else:
            raise ValueError('Required property \'timestamp\' not present in ProjectConfigMetadataLastApproved JSON')
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
        if hasattr(self, 'is_forced') and self.is_forced is not None:
            _dict['is_forced'] = self.is_forced
        if hasattr(self, 'comment') and self.comment is not None:
            _dict['comment'] = self.comment
        if hasattr(self, 'timestamp') and self.timestamp is not None:
            _dict['timestamp'] = datetime_to_string(self.timestamp)
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


class ProjectConfigPrototype:
    """
    The input of a project configuration.

    :attr ProjectConfigPrototypeDefinitionBlock definition: The name and description
          of a project configuration.
    :attr SchematicsWorkspace schematics: (optional) A schematics workspace
          associated to a project configuration.
    """

    def __init__(
        self,
        definition: 'ProjectConfigPrototypeDefinitionBlock',
        *,
        schematics: 'SchematicsWorkspace' = None,
    ) -> None:
        """
        Initialize a ProjectConfigPrototype object.

        :param ProjectConfigPrototypeDefinitionBlock definition: The name and
               description of a project configuration.
        :param SchematicsWorkspace schematics: (optional) A schematics workspace
               associated to a project configuration.
        """
        self.definition = definition
        self.schematics = schematics

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigPrototype':
        """Initialize a ProjectConfigPrototype object from a json dictionary."""
        args = {}
        if 'definition' in _dict:
            args['definition'] = ProjectConfigPrototypeDefinitionBlock.from_dict(_dict.get('definition'))
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
    The name and description of a project configuration.

    :attr str name: The configuration name.
    :attr str description: (optional) A project configuration description.
    :attr List[str] labels: (optional) The configuration labels.
    :attr str environment: (optional) The ID of the project environment.
    :attr ProjectConfigAuth authorizations: (optional) The authorization for a
          configuration.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr ProjectComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    :attr str locator_id: (optional) A dotted value of catalogID.versionID.
    :attr InputVariable input: (optional) The input variables for configuration
          definition and environment.
    :attr ProjectConfigSetting setting: (optional) Schematics environment variables
          to use to deploy the configuration.
          Settings are only available if they were specified when the configuration was
          initially created.
    """

    def __init__(
        self,
        name: str,
        *,
        description: str = None,
        labels: List[str] = None,
        environment: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        compliance_profile: 'ProjectComplianceProfile' = None,
        locator_id: str = None,
        input: 'InputVariable' = None,
        setting: 'ProjectConfigSetting' = None,
    ) -> None:
        """
        Initialize a ProjectConfigPrototypeDefinitionBlock object.

        :param str name: The configuration name.
        :param str description: (optional) A project configuration description.
        :param List[str] labels: (optional) The configuration labels.
        :param str environment: (optional) The ID of the project environment.
        :param ProjectConfigAuth authorizations: (optional) The authorization for a
               configuration.
               You can authorize by using a trusted profile or an API key in Secrets
               Manager.
        :param ProjectComplianceProfile compliance_profile: (optional) The profile
               required for compliance.
        :param str locator_id: (optional) A dotted value of catalogID.versionID.
        :param InputVariable input: (optional) The input variables for
               configuration definition and environment.
        :param ProjectConfigSetting setting: (optional) Schematics environment
               variables to use to deploy the configuration.
               Settings are only available if they were specified when the configuration
               was initially created.
        """
        self.name = name
        self.description = description
        self.labels = labels
        self.environment = environment
        self.authorizations = authorizations
        self.compliance_profile = compliance_profile
        self.locator_id = locator_id
        self.input = input
        self.setting = setting

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigPrototypeDefinitionBlock':
        """Initialize a ProjectConfigPrototypeDefinitionBlock object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ProjectConfigPrototypeDefinitionBlock JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'labels' in _dict:
            args['labels'] = _dict.get('labels')
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'compliance_profile' in _dict:
            args['compliance_profile'] = ProjectComplianceProfile.from_dict(_dict.get('compliance_profile'))
        if 'locator_id' in _dict:
            args['locator_id'] = _dict.get('locator_id')
        if 'input' in _dict:
            args['input'] = InputVariable.from_dict(_dict.get('input'))
        if 'setting' in _dict:
            args['setting'] = ProjectConfigSetting.from_dict(_dict.get('setting'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigPrototypeDefinitionBlock object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'authorizations') and self.authorizations is not None:
            if isinstance(self.authorizations, dict):
                _dict['authorizations'] = self.authorizations
            else:
                _dict['authorizations'] = self.authorizations.to_dict()
        if hasattr(self, 'compliance_profile') and self.compliance_profile is not None:
            if isinstance(self.compliance_profile, dict):
                _dict['compliance_profile'] = self.compliance_profile
            else:
                _dict['compliance_profile'] = self.compliance_profile.to_dict()
        if hasattr(self, 'locator_id') and self.locator_id is not None:
            _dict['locator_id'] = self.locator_id
        if hasattr(self, 'input') and self.input is not None:
            if isinstance(self.input, dict):
                _dict['input'] = self.input
            else:
                _dict['input'] = self.input.to_dict()
        if hasattr(self, 'setting') and self.setting is not None:
            if isinstance(self.setting, dict):
                _dict['setting'] = self.setting
            else:
                _dict['setting'] = self.setting.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigPrototypeDefinitionBlock object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigPrototypeDefinitionBlock') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigPrototypeDefinitionBlock') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigPrototypePatchDefinitionBlock:
    """
    The name and description of a project configuration.

    :attr str name: (optional) The configuration name.
    :attr str description: (optional) A project configuration description.
    :attr List[str] labels: (optional) The configuration labels.
    :attr str environment: (optional) The ID of the project environment.
    :attr ProjectConfigAuth authorizations: (optional) The authorization for a
          configuration.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr ProjectComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    :attr str locator_id: (optional) A dotted value of catalogID.versionID.
    :attr InputVariable input: (optional) The input variables for configuration
          definition and environment.
    :attr ProjectConfigSetting setting: (optional) Schematics environment variables
          to use to deploy the configuration.
          Settings are only available if they were specified when the configuration was
          initially created.
    """

    def __init__(
        self,
        *,
        name: str = None,
        description: str = None,
        labels: List[str] = None,
        environment: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        compliance_profile: 'ProjectComplianceProfile' = None,
        locator_id: str = None,
        input: 'InputVariable' = None,
        setting: 'ProjectConfigSetting' = None,
    ) -> None:
        """
        Initialize a ProjectConfigPrototypePatchDefinitionBlock object.

        :param str name: (optional) The configuration name.
        :param str description: (optional) A project configuration description.
        :param List[str] labels: (optional) The configuration labels.
        :param str environment: (optional) The ID of the project environment.
        :param ProjectConfigAuth authorizations: (optional) The authorization for a
               configuration.
               You can authorize by using a trusted profile or an API key in Secrets
               Manager.
        :param ProjectComplianceProfile compliance_profile: (optional) The profile
               required for compliance.
        :param str locator_id: (optional) A dotted value of catalogID.versionID.
        :param InputVariable input: (optional) The input variables for
               configuration definition and environment.
        :param ProjectConfigSetting setting: (optional) Schematics environment
               variables to use to deploy the configuration.
               Settings are only available if they were specified when the configuration
               was initially created.
        """
        self.name = name
        self.description = description
        self.labels = labels
        self.environment = environment
        self.authorizations = authorizations
        self.compliance_profile = compliance_profile
        self.locator_id = locator_id
        self.input = input
        self.setting = setting

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigPrototypePatchDefinitionBlock':
        """Initialize a ProjectConfigPrototypePatchDefinitionBlock object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'labels' in _dict:
            args['labels'] = _dict.get('labels')
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'compliance_profile' in _dict:
            args['compliance_profile'] = ProjectComplianceProfile.from_dict(_dict.get('compliance_profile'))
        if 'locator_id' in _dict:
            args['locator_id'] = _dict.get('locator_id')
        if 'input' in _dict:
            args['input'] = InputVariable.from_dict(_dict.get('input'))
        if 'setting' in _dict:
            args['setting'] = ProjectConfigSetting.from_dict(_dict.get('setting'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigPrototypePatchDefinitionBlock object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'authorizations') and self.authorizations is not None:
            if isinstance(self.authorizations, dict):
                _dict['authorizations'] = self.authorizations
            else:
                _dict['authorizations'] = self.authorizations.to_dict()
        if hasattr(self, 'compliance_profile') and self.compliance_profile is not None:
            if isinstance(self.compliance_profile, dict):
                _dict['compliance_profile'] = self.compliance_profile
            else:
                _dict['compliance_profile'] = self.compliance_profile.to_dict()
        if hasattr(self, 'locator_id') and self.locator_id is not None:
            _dict['locator_id'] = self.locator_id
        if hasattr(self, 'input') and self.input is not None:
            if isinstance(self.input, dict):
                _dict['input'] = self.input
            else:
                _dict['input'] = self.input.to_dict()
        if hasattr(self, 'setting') and self.setting is not None:
            if isinstance(self.setting, dict):
                _dict['setting'] = self.setting
            else:
                _dict['setting'] = self.setting.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigPrototypePatchDefinitionBlock object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigPrototypePatchDefinitionBlock') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigPrototypePatchDefinitionBlock') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


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

    :attr List[ProjectConfigResource] resources: (optional) The collection list
          operation response schema that defines the array property with the name
          `resources`.
    :attr int resources_count: The total number of resources deployed by the
          configuration.
    """

    def __init__(
        self,
        resources_count: int,
        *,
        resources: List['ProjectConfigResource'] = None,
    ) -> None:
        """
        Initialize a ProjectConfigResourceCollection object.

        :param int resources_count: The total number of resources deployed by the
               configuration.
        :param List[ProjectConfigResource] resources: (optional) The collection
               list operation response schema that defines the array property with the
               name `resources`.
        """
        self.resources = resources
        self.resources_count = resources_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigResourceCollection':
        """Initialize a ProjectConfigResourceCollection object from a json dictionary."""
        args = {}
        if 'resources' in _dict:
            args['resources'] = [ProjectConfigResource.from_dict(v) for v in _dict.get('resources')]
        if 'resources_count' in _dict:
            args['resources_count'] = _dict.get('resources_count')
        else:
            raise ValueError('Required property \'resources_count\' not present in ProjectConfigResourceCollection JSON')
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
    The type and output of a project configuration.

    :attr str name: The configuration name.
    :attr str description: (optional) A project configuration description.
    :attr List[str] labels: (optional) The configuration labels.
    :attr str environment: (optional) The ID of the project environment.
    :attr ProjectConfigAuth authorizations: (optional) The authorization for a
          configuration.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr ProjectComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    :attr str locator_id: A dotted value of catalogID.versionID.
    :attr InputVariable input: (optional) The input variables for configuration
          definition and environment.
    :attr ProjectConfigSetting setting: (optional) Schematics environment variables
          to use to deploy the configuration.
          Settings are only available if they were specified when the configuration was
          initially created.
    :attr str type: (optional) The type of a project configuration manual property.
    :attr List[OutputValue] output: (optional) The outputs of a Schematics template
          property.
    """

    def __init__(
        self,
        name: str,
        locator_id: str,
        *,
        description: str = None,
        labels: List[str] = None,
        environment: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        compliance_profile: 'ProjectComplianceProfile' = None,
        input: 'InputVariable' = None,
        setting: 'ProjectConfigSetting' = None,
        type: str = None,
        output: List['OutputValue'] = None,
    ) -> None:
        """
        Initialize a ProjectConfigResponseDefinition object.

        :param str name: The configuration name.
        :param str locator_id: A dotted value of catalogID.versionID.
        :param str description: (optional) A project configuration description.
        :param List[str] labels: (optional) The configuration labels.
        :param str environment: (optional) The ID of the project environment.
        :param ProjectConfigAuth authorizations: (optional) The authorization for a
               configuration.
               You can authorize by using a trusted profile or an API key in Secrets
               Manager.
        :param ProjectComplianceProfile compliance_profile: (optional) The profile
               required for compliance.
        :param InputVariable input: (optional) The input variables for
               configuration definition and environment.
        :param ProjectConfigSetting setting: (optional) Schematics environment
               variables to use to deploy the configuration.
               Settings are only available if they were specified when the configuration
               was initially created.
        :param str type: (optional) The type of a project configuration manual
               property.
        :param List[OutputValue] output: (optional) The outputs of a Schematics
               template property.
        """
        self.name = name
        self.description = description
        self.labels = labels
        self.environment = environment
        self.authorizations = authorizations
        self.compliance_profile = compliance_profile
        self.locator_id = locator_id
        self.input = input
        self.setting = setting
        self.type = type
        self.output = output

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigResponseDefinition':
        """Initialize a ProjectConfigResponseDefinition object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ProjectConfigResponseDefinition JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'labels' in _dict:
            args['labels'] = _dict.get('labels')
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'compliance_profile' in _dict:
            args['compliance_profile'] = ProjectComplianceProfile.from_dict(_dict.get('compliance_profile'))
        if 'locator_id' in _dict:
            args['locator_id'] = _dict.get('locator_id')
        else:
            raise ValueError('Required property \'locator_id\' not present in ProjectConfigResponseDefinition JSON')
        if 'input' in _dict:
            args['input'] = InputVariable.from_dict(_dict.get('input'))
        if 'setting' in _dict:
            args['setting'] = ProjectConfigSetting.from_dict(_dict.get('setting'))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'output' in _dict:
            args['output'] = [OutputValue.from_dict(v) for v in _dict.get('output')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigResponseDefinition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'authorizations') and self.authorizations is not None:
            if isinstance(self.authorizations, dict):
                _dict['authorizations'] = self.authorizations
            else:
                _dict['authorizations'] = self.authorizations.to_dict()
        if hasattr(self, 'compliance_profile') and self.compliance_profile is not None:
            if isinstance(self.compliance_profile, dict):
                _dict['compliance_profile'] = self.compliance_profile
            else:
                _dict['compliance_profile'] = self.compliance_profile.to_dict()
        if hasattr(self, 'locator_id') and self.locator_id is not None:
            _dict['locator_id'] = self.locator_id
        if hasattr(self, 'input') and self.input is not None:
            if isinstance(self.input, dict):
                _dict['input'] = self.input
            else:
                _dict['input'] = self.input.to_dict()
        if hasattr(self, 'setting') and self.setting is not None:
            if isinstance(self.setting, dict):
                _dict['setting'] = self.setting
            else:
                _dict['setting'] = self.setting.to_dict()
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'output') and self.output is not None:
            output_list = []
            for v in self.output:
                if isinstance(v, dict):
                    output_list.append(v)
                else:
                    output_list.append(v.to_dict())
            _dict['output'] = output_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigResponseDefinition object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigResponseDefinition') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigResponseDefinition') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of a project configuration manual property.
        """

        TERRAFORM_TEMPLATE = 'terraform_template'
        SCHEMATICS_BLUEPRINT = 'schematics_blueprint'



class ProjectConfigSetting:
    """
    Schematics environment variables to use to deploy the configuration. Settings are only
    available if they were specified when the configuration was initially created.

    """

    def __init__(
        self,
        **kwargs,
    ) -> None:
        """
        Initialize a ProjectConfigSetting object.

        :param **kwargs: (optional) Any additional properties.
        """
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigSetting':
        """Initialize a ProjectConfigSetting object from a json dictionary."""
        return cls(**_dict)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigSetting object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        return vars(self)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of ProjectConfigSetting"""
        _dict = {}

        for _key in [k for k in vars(self).keys()]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of ProjectConfigSetting"""
        for _key in [k for k in vars(self).keys()]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            setattr(self, _key, _value)

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigSetting object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigSetting') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigSetting') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigVersion:
    """
    A specific version of a project configuration.

    :attr str id: The ID of the configuration. If this parameter is empty, an ID is
          automatically created for the configuration.
    :attr str project_id: The unique ID.
    :attr int version: The version of the configuration.
    :attr bool is_draft: The flag that indicates whether the version of the
          configuration is draft, or active.
    :attr List[object] needs_attention_state: (optional) The needs attention state
          of a configuration.
    :attr str state: The state of the configuration.
    :attr bool update_available: The flag that indicates whether a configuration
          update is available.
    :attr datetime created_at: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr datetime user_modified_at: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr ProjectConfigMetadataLastApproved last_approved: (optional) The last
          approved metadata of the configuration.
    :attr datetime last_save: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr dict references: (optional) The references used in the config to resolve
          input values.
    :attr LastValidatedActionWithSummary last_validated: (optional) The action job
          performed on the project configuration.
    :attr LastActionWithSummary last_deployed: (optional) The action job performed
          on the project configuration.
    :attr LastActionWithSummary last_undeployed: (optional) The action job performed
          on the project configuration.
    :attr SchematicsWorkspace schematics: (optional) A schematics workspace
          associated to a project configuration.
    :attr ProjectConfigResponseDefinition definition: The type and output of a
          project configuration.
    """

    def __init__(
        self,
        id: str,
        project_id: str,
        version: int,
        is_draft: bool,
        state: str,
        update_available: bool,
        definition: 'ProjectConfigResponseDefinition',
        *,
        needs_attention_state: List[object] = None,
        created_at: datetime = None,
        user_modified_at: datetime = None,
        last_approved: 'ProjectConfigMetadataLastApproved' = None,
        last_save: datetime = None,
        references: dict = None,
        last_validated: 'LastValidatedActionWithSummary' = None,
        last_deployed: 'LastActionWithSummary' = None,
        last_undeployed: 'LastActionWithSummary' = None,
        schematics: 'SchematicsWorkspace' = None,
    ) -> None:
        """
        Initialize a ProjectConfigVersion object.

        :param str id: The ID of the configuration. If this parameter is empty, an
               ID is automatically created for the configuration.
        :param str project_id: The unique ID.
        :param int version: The version of the configuration.
        :param bool is_draft: The flag that indicates whether the version of the
               configuration is draft, or active.
        :param str state: The state of the configuration.
        :param bool update_available: The flag that indicates whether a
               configuration update is available.
        :param ProjectConfigResponseDefinition definition: The type and output of a
               project configuration.
        :param List[object] needs_attention_state: (optional) The needs attention
               state of a configuration.
        :param datetime created_at: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param datetime user_modified_at: (optional) A date and time value in the
               format YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date
               and time format as specified by RFC 3339.
        :param ProjectConfigMetadataLastApproved last_approved: (optional) The last
               approved metadata of the configuration.
        :param datetime last_save: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param dict references: (optional) The references used in the config to
               resolve input values.
        :param LastValidatedActionWithSummary last_validated: (optional) The action
               job performed on the project configuration.
        :param LastActionWithSummary last_deployed: (optional) The action job
               performed on the project configuration.
        :param LastActionWithSummary last_undeployed: (optional) The action job
               performed on the project configuration.
        :param SchematicsWorkspace schematics: (optional) A schematics workspace
               associated to a project configuration.
        """
        self.id = id
        self.project_id = project_id
        self.version = version
        self.is_draft = is_draft
        self.needs_attention_state = needs_attention_state
        self.state = state
        self.update_available = update_available
        self.created_at = created_at
        self.user_modified_at = user_modified_at
        self.last_approved = last_approved
        self.last_save = last_save
        self.references = references
        self.last_validated = last_validated
        self.last_deployed = last_deployed
        self.last_undeployed = last_undeployed
        self.schematics = schematics
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigVersion':
        """Initialize a ProjectConfigVersion object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectConfigVersion JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in ProjectConfigVersion JSON')
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
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectConfigVersion JSON')
        if 'update_available' in _dict:
            args['update_available'] = _dict.get('update_available')
        else:
            raise ValueError('Required property \'update_available\' not present in ProjectConfigVersion JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'user_modified_at' in _dict:
            args['user_modified_at'] = string_to_datetime(_dict.get('user_modified_at'))
        if 'last_approved' in _dict:
            args['last_approved'] = ProjectConfigMetadataLastApproved.from_dict(_dict.get('last_approved'))
        if 'last_save' in _dict:
            args['last_save'] = string_to_datetime(_dict.get('last_save'))
        if 'references' in _dict:
            args['references'] = _dict.get('references')
        if 'last_validated' in _dict:
            args['last_validated'] = LastValidatedActionWithSummary.from_dict(_dict.get('last_validated'))
        if 'last_deployed' in _dict:
            args['last_deployed'] = LastActionWithSummary.from_dict(_dict.get('last_deployed'))
        if 'last_undeployed' in _dict:
            args['last_undeployed'] = LastActionWithSummary.from_dict(_dict.get('last_undeployed'))
        if 'schematics' in _dict:
            args['schematics'] = SchematicsWorkspace.from_dict(_dict.get('schematics'))
        if 'definition' in _dict:
            args['definition'] = ProjectConfigResponseDefinition.from_dict(_dict.get('definition'))
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
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'is_draft') and self.is_draft is not None:
            _dict['is_draft'] = self.is_draft
        if hasattr(self, 'needs_attention_state') and self.needs_attention_state is not None:
            _dict['needs_attention_state'] = self.needs_attention_state
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'update_available') and self.update_available is not None:
            _dict['update_available'] = self.update_available
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'user_modified_at') and self.user_modified_at is not None:
            _dict['user_modified_at'] = datetime_to_string(self.user_modified_at)
        if hasattr(self, 'last_approved') and self.last_approved is not None:
            if isinstance(self.last_approved, dict):
                _dict['last_approved'] = self.last_approved
            else:
                _dict['last_approved'] = self.last_approved.to_dict()
        if hasattr(self, 'last_save') and self.last_save is not None:
            _dict['last_save'] = datetime_to_string(self.last_save)
        if hasattr(self, 'references') and self.references is not None:
            _dict['references'] = self.references
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
        if hasattr(self, 'schematics') and self.schematics is not None:
            if isinstance(self.schematics, dict):
                _dict['schematics'] = self.schematics
            else:
                _dict['schematics'] = self.schematics.to_dict()
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
        SUPERCEDED = 'superceded'
        UNDEPLOYING = 'undeploying'
        UNDEPLOYING_FAILED = 'undeploying_failed'
        VALIDATED = 'validated'
        VALIDATING = 'validating'
        VALIDATING_FAILED = 'validating_failed'



class ProjectConfigVersionSummary:
    """
    The project configuration version.

    :attr List[object] needs_attention_state: (optional) The needs attention state
          of a configuration.
    :attr str state: The state of the configuration.
    :attr int version: The version number of the configuration.
    :attr str href: (optional) A relative URL.
    """

    def __init__(
        self,
        state: str,
        version: int,
        *,
        needs_attention_state: List[object] = None,
        href: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigVersionSummary object.

        :param str state: The state of the configuration.
        :param int version: The version number of the configuration.
        :param List[object] needs_attention_state: (optional) The needs attention
               state of a configuration.
        :param str href: (optional) A relative URL.
        """
        self.needs_attention_state = needs_attention_state
        self.state = state
        self.version = version
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigVersionSummary':
        """Initialize a ProjectConfigVersionSummary object from a json dictionary."""
        args = {}
        if 'needs_attention_state' in _dict:
            args['needs_attention_state'] = _dict.get('needs_attention_state')
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
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigVersionSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'needs_attention_state') and self.needs_attention_state is not None:
            _dict['needs_attention_state'] = self.needs_attention_state
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
        SUPERCEDED = 'superceded'
        UNDEPLOYING = 'undeploying'
        UNDEPLOYING_FAILED = 'undeploying_failed'
        VALIDATED = 'validated'
        VALIDATING = 'validating'
        VALIDATING_FAILED = 'validating_failed'



class ProjectConfigVersionSummaryCollection:
    """
    The project configuration version list.

    :attr List[ProjectConfigVersionSummary] versions: (optional) The collection list
          operation response schema that defines the array property with the name
          `versions`.
    """

    def __init__(
        self,
        *,
        versions: List['ProjectConfigVersionSummary'] = None,
    ) -> None:
        """
        Initialize a ProjectConfigVersionSummaryCollection object.

        :param List[ProjectConfigVersionSummary] versions: (optional) The
               collection list operation response schema that defines the array property
               with the name `versions`.
        """
        self.versions = versions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigVersionSummaryCollection':
        """Initialize a ProjectConfigVersionSummaryCollection object from a json dictionary."""
        args = {}
        if 'versions' in _dict:
            args['versions'] = [ProjectConfigVersionSummary.from_dict(v) for v in _dict.get('versions')]
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

    :attr str name: The name of the project.
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

        :param str name: The name of the project.
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


class ProjectEnvironmentCollectionMember:
    """
    The environment metadata.

    :attr str id: The environment id as a friendly name.
    :attr str project_id: The unique ID.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr str href: A relative URL.
    :attr EnvironmentDefinitionNameDescription definition: The environment
          definition used in the project collection.
    """

    def __init__(
        self,
        id: str,
        project_id: str,
        created_at: datetime,
        href: str,
        definition: 'EnvironmentDefinitionNameDescription',
    ) -> None:
        """
        Initialize a ProjectEnvironmentCollectionMember object.

        :param str id: The environment id as a friendly name.
        :param str project_id: The unique ID.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param str href: A relative URL.
        :param EnvironmentDefinitionNameDescription definition: The environment
               definition used in the project collection.
        """
        self.id = id
        self.project_id = project_id
        self.created_at = created_at
        self.href = href
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectEnvironmentCollectionMember':
        """Initialize a ProjectEnvironmentCollectionMember object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectEnvironmentCollectionMember JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in ProjectEnvironmentCollectionMember JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProjectEnvironmentCollectionMember JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ProjectEnvironmentCollectionMember JSON')
        if 'definition' in _dict:
            args['definition'] = EnvironmentDefinitionNameDescription.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in ProjectEnvironmentCollectionMember JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectEnvironmentCollectionMember object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
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
        """Return a `str` version of this ProjectEnvironmentCollectionMember object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectEnvironmentCollectionMember') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectEnvironmentCollectionMember') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectPrototypeDefinition:
    """
    The definition of the project.

    :attr str name: The name of the project.
    :attr str description: (optional) A brief explanation of the project's use in
          the configuration of a deployable architecture. It is possible to create a
          project without providing a description.
    :attr bool destroy_on_delete: (optional) The policy that indicates whether the
          resources are destroyed or not when a project is deleted.
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

        :param str name: The name of the project.
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


class ProjectPrototypePatchDefinitionBlock:
    """
    The definition of the project.

    :attr str name: (optional) The name of the project.
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
        Initialize a ProjectPrototypePatchDefinitionBlock object.

        :param str name: (optional) The name of the project.
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
    def from_dict(cls, _dict: Dict) -> 'ProjectPrototypePatchDefinitionBlock':
        """Initialize a ProjectPrototypePatchDefinitionBlock object from a json dictionary."""
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
        """Initialize a ProjectPrototypePatchDefinitionBlock object from a json dictionary."""
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
        """Return a `str` version of this ProjectPrototypePatchDefinitionBlock object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectPrototypePatchDefinitionBlock') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectPrototypePatchDefinitionBlock') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SchematicsWorkspace:
    """
    A schematics workspace associated to a project configuration.

    :attr str workspace_id: (optional) An existing schematics workspace ID.
    """

    def __init__(
        self,
        *,
        workspace_id: str = None,
    ) -> None:
        """
        Initialize a SchematicsWorkspace object.

        :param str workspace_id: (optional) An existing schematics workspace ID.
        """
        self.workspace_id = workspace_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchematicsWorkspace':
        """Initialize a SchematicsWorkspace object from a json dictionary."""
        args = {}
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict.get('workspace_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchematicsWorkspace object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'workspace_id') and self.workspace_id is not None:
            _dict['workspace_id'] = self.workspace_id
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
        :return: A List[dict], where each element is a dict that represents an instance of ProjectCollectionMemberWithMetadata.
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
        :return: A List[dict], where each element is a dict that represents an instance of ProjectCollectionMemberWithMetadata.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
