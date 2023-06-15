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

# IBM OpenAPI SDK Code Generator Version: 3.72.2-2bede9d2-20230601-202845

"""
This document is the **REST API specification** for the Projects Service. The Projects
service provides the capability to manage Infrastructure as Code in IBM Cloud.

API Version: 1.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
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
        resource_group: str,
        location: str,
        name: str,
        *,
        description: str = None,
        destroy_on_delete: bool = None,
        configs: List['ProjectConfigPrototype'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a project.

        Create a new project and asynchronously setup the tools to manage it. Add a
        deployable architecture by customizing the configuration. After the changes are
        validated and approved, deploy the resources that the project configures.

        :param str resource_group: The resource group where the project's data and
               tools are created.
        :param str location: The location where the project's data and tools are
               created.
        :param str name: The name of the project.
        :param str description: (optional) A brief explanation of the project's use
               in the configuration of a deployable architecture. It is possible to create
               a project without providing a description.
        :param bool destroy_on_delete: (optional) The policy that indicates whether
               the resources are destroyed or not when a project is deleted.
        :param List[ProjectConfigPrototype] configs: (optional) The project
               configurations. If configurations are not included, the project resource is
               persisted without this property.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Project` object
        """

        if not resource_group:
            raise ValueError('resource_group must be provided')
        if not location:
            raise ValueError('location must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if configs is not None:
            configs = [convert_model(x) for x in configs]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_project',
        )
        headers.update(sdk_headers)

        params = {
            'resource_group': resource_group,
            'location': location,
        }

        data = {
            'name': name,
            'description': description,
            'destroy_on_delete': destroy_on_delete,
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
            params=params,
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
        :rtype: DetailedResponse with `dict` result representing a `ProjectSummary` object
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
    # Configurations
    #########################

    def create_config(
        self,
        project_id: str,
        name: str,
        locator_id: str,
        *,
        labels: List[str] = None,
        description: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        compliance_profile: 'ProjectConfigComplianceProfile' = None,
        input: List['ProjectConfigInputVariable'] = None,
        setting: List['ProjectConfigSettingCollection'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Add a new configuration.

        Add a new configuration to a project.

        :param str project_id: The unique project ID.
        :param str name: The name of the configuration.
        :param str locator_id: A dotted value of catalogID.versionID.
        :param List[str] labels: (optional) A collection of configuration labels.
        :param str description: (optional) The description of the project
               configuration.
        :param ProjectConfigAuth authorizations: (optional) The authorization for a
               configuration.
               You can authorize by using a trusted profile or an API key in Secrets
               Manager.
        :param ProjectConfigComplianceProfile compliance_profile: (optional) The
               profile required for compliance.
        :param List[ProjectConfigInputVariable] input: (optional) The inputs of a
               Schematics template property.
        :param List[ProjectConfigSettingCollection] setting: (optional) Schematics
               environment variables to use to deploy the configuration. Settings are only
               available if they were specified when the configuration was initially
               created.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigDraftResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if locator_id is None:
            raise ValueError('locator_id must be provided')
        if authorizations is not None:
            authorizations = convert_model(authorizations)
        if compliance_profile is not None:
            compliance_profile = convert_model(compliance_profile)
        if input is not None:
            input = [convert_model(x) for x in input]
        if setting is not None:
            setting = [convert_model(x) for x in setting]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_config',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'locator_id': locator_id,
            'labels': labels,
            'description': description,
            'authorizations': authorizations,
            'compliance_profile': compliance_profile,
            'input': input,
            'setting': setting,
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
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigGetResponse` object
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
        *,
        locator_id: str = None,
        input: List['ProjectConfigInputVariable'] = None,
        setting: List['ProjectConfigSettingCollection'] = None,
        name: str = None,
        labels: List[str] = None,
        description: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        compliance_profile: 'ProjectConfigComplianceProfile' = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a configuration.

        Update a configuration in a project by the ID.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param str locator_id: (optional) A dotted value of catalogID.versionID.
        :param List[ProjectConfigInputVariable] input: (optional) The inputs of a
               Schematics template property.
        :param List[ProjectConfigSettingCollection] setting: (optional) Schematics
               environment variables to use to deploy the configuration. Settings are only
               available if they were specified when the configuration was initially
               created.
        :param str name: (optional) The configuration name.
        :param List[str] labels: (optional) The configuration labels.
        :param str description: (optional) A project configuration description.
        :param ProjectConfigAuth authorizations: (optional) The authorization for a
               configuration.
               You can authorize by using a trusted profile or an API key in Secrets
               Manager.
        :param ProjectConfigComplianceProfile compliance_profile: (optional) The
               profile required for compliance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigDraftResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        if input is not None:
            input = [convert_model(x) for x in input]
        if setting is not None:
            setting = [convert_model(x) for x in setting]
        if authorizations is not None:
            authorizations = convert_model(authorizations)
        if compliance_profile is not None:
            compliance_profile = convert_model(compliance_profile)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_config',
        )
        headers.update(sdk_headers)

        data = {
            'locator_id': locator_id,
            'input': input,
            'setting': setting,
            'name': name,
            'labels': labels,
            'description': description,
            'authorizations': authorizations,
            'compliance_profile': compliance_profile,
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
        *,
        draft_only: bool = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a configuration in a project by ID.

        Delete a configuration in a project. Deleting the configuration will also destroy
        all the resources deployed by the configuration if the query parameter `destroy`
        is specified.

        :param str project_id: The unique project ID.
        :param str id: The unique config ID.
        :param bool draft_only: (optional) The flag to determine if only the draft
               version should be deleted.
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

        params = {
            'draft_only': draft_only,
        }

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
            params=params,
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
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigGetResponse` object
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

    def check_config(
        self,
        project_id: str,
        id: str,
        *,
        x_auth_refresh_token: str = None,
        is_draft: bool = None,
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
        :param bool is_draft: (optional) To specify whether the validation check
               triggers against the `draft` or the `active` version of the configuration.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigGetResponse` object
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
            operation_id='check_config',
        )
        headers.update(sdk_headers)

        params = {
            'is_draft': is_draft,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/check'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def install_config(
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
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigGetResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='install_config',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/install'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def uninstall_config(
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
            operation_id='uninstall_config',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['project_id', 'id']
        path_param_values = self.encode_path_vars(project_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{id}/uninstall'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
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

    def list_config_drafts(
        self,
        project_id: str,
        config_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a list of project configuration drafts.

        Returns a list of previous and current configuration drafts in a specific project.

        :param str project_id: The unique project ID.
        :param str config_id: The unique configuration ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigDraftSummaryCollection` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not config_id:
            raise ValueError('config_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_config_drafts',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'config_id']
        path_param_values = self.encode_path_vars(project_id, config_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{config_id}/drafts'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_config_draft(
        self,
        project_id: str,
        config_id: str,
        version: int,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a project configuration draft.

        Returns the specific version of a configuration draft in a specific project.

        :param str project_id: The unique project ID.
        :param str config_id: The unique configuration ID.
        :param int version: The configuration version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProjectConfigDraftResponse` object
        """

        if not project_id:
            raise ValueError('project_id must be provided')
        if not config_id:
            raise ValueError('config_id must be provided')
        if version is None:
            raise ValueError('version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_config_draft',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['project_id', 'config_id', 'version']
        path_param_values = self.encode_path_vars(project_id, config_id, str(version))
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/projects/{project_id}/configs/{config_id}/drafts/{version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class CumulativeNeedsAttention:
    """
    CumulativeNeedsAttention.

    :attr str event: (optional) The event name.
    :attr str event_id: (optional) The unique ID of a project.
    :attr str config_id: (optional) The unique ID of a project.
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
        :param str event_id: (optional) The unique ID of a project.
        :param str config_id: (optional) The unique ID of a project.
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


class InputVariable:
    """
    InputVariable.

    :attr str name: The variable name.
    :attr str type: The variable type.
    :attr object value: (optional) Can be any value - a string, number, boolean,
          array, or object.
    :attr bool required: (optional) Whether the variable is required or not.
    """

    def __init__(
        self,
        name: str,
        type: str,
        *,
        value: object = None,
        required: bool = None,
    ) -> None:
        """
        Initialize a InputVariable object.

        :param str name: The variable name.
        :param str type: The variable type.
        :param object value: (optional) Can be any value - a string, number,
               boolean, array, or object.
        :param bool required: (optional) Whether the variable is required or not.
        """
        self.name = name
        self.type = type
        self.value = value
        self.required = required

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InputVariable':
        """Initialize a InputVariable object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in InputVariable JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in InputVariable JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'required' in _dict:
            args['required'] = _dict.get('required')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InputVariable object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'required') and self.required is not None:
            _dict['required'] = self.required
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

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

    class TypeEnum(str, Enum):
        """
        The variable type.
        """

        ARRAY = 'array'
        BOOLEAN = 'boolean'
        FLOAT = 'float'
        INT = 'int'
        NUMBER = 'number'
        PASSWORD = 'password'
        STRING = 'string'
        OBJECT = 'object'



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
    :attr str start: (optional) A pagination token.
    """

    def __init__(
        self,
        href: str,
        *,
        start: str = None,
    ) -> None:
        """
        Initialize a PaginationLink object.

        :param str href: A relative URL.
        :param str start: (optional) A pagination token.
        """
        self.href = href
        self.start = start

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PaginationLink':
        """Initialize a PaginationLink object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in PaginationLink JSON')
        if 'start' in _dict:
            args['start'] = _dict.get('start')
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
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
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


class Project:
    """
    The project returned in the response body.

    :attr str crn: An IBM Cloud resource name, which uniquely identifies a resource.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr List[CumulativeNeedsAttention] cumulative_needs_attention_view: (optional)
          The cumulative list of needs attention items for a project. If the view is
          successfully retrieved, an array which could be empty is returned.
    :attr bool cumulative_needs_attention_view_error: (optional) True indicates that
          the fetch of the needs attention items failed. It only exists if there was an
          error while retrieving the cumulative needs attention view.
    :attr str id: The unique ID of a project.
    :attr str location: The IBM Cloud location where a resource is deployed.
    :attr str resource_group: The resource group where the project's data and tools
          are created.
    :attr str state: The project status value.
    :attr str event_notifications_crn: (optional) The CRN of the event notifications
          instance if one is connected to this project.
    :attr ProjectDefinitionResponse definition: (optional) The definition of the
          project.
    :attr List[ProjectConfigCollectionMember] configs: (optional) The project
          configurations. These configurations are only included in the response of
          creating a project if a configs array is specified in the request payload.
    """

    def __init__(
        self,
        crn: str,
        created_at: datetime,
        id: str,
        location: str,
        resource_group: str,
        state: str,
        *,
        cumulative_needs_attention_view: List['CumulativeNeedsAttention'] = None,
        cumulative_needs_attention_view_error: bool = None,
        event_notifications_crn: str = None,
        definition: 'ProjectDefinitionResponse' = None,
        configs: List['ProjectConfigCollectionMember'] = None,
    ) -> None:
        """
        Initialize a Project object.

        :param str crn: An IBM Cloud resource name, which uniquely identifies a
               resource.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param str id: The unique ID of a project.
        :param str location: The IBM Cloud location where a resource is deployed.
        :param str resource_group: The resource group where the project's data and
               tools are created.
        :param str state: The project status value.
        :param List[CumulativeNeedsAttention] cumulative_needs_attention_view:
               (optional) The cumulative list of needs attention items for a project. If
               the view is successfully retrieved, an array which could be empty is
               returned.
        :param bool cumulative_needs_attention_view_error: (optional) True
               indicates that the fetch of the needs attention items failed. It only
               exists if there was an error while retrieving the cumulative needs
               attention view.
        :param str event_notifications_crn: (optional) The CRN of the event
               notifications instance if one is connected to this project.
        :param ProjectDefinitionResponse definition: (optional) The definition of
               the project.
        :param List[ProjectConfigCollectionMember] configs: (optional) The project
               configurations. These configurations are only included in the response of
               creating a project if a configs array is specified in the request payload.
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
        self.configs = configs

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
            args['cumulative_needs_attention_view'] = [CumulativeNeedsAttention.from_dict(v) for v in _dict.get('cumulative_needs_attention_view')]
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
        if 'resource_group' in _dict:
            args['resource_group'] = _dict.get('resource_group')
        else:
            raise ValueError('Required property \'resource_group\' not present in Project JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in Project JSON')
        if 'event_notifications_crn' in _dict:
            args['event_notifications_crn'] = _dict.get('event_notifications_crn')
        if 'definition' in _dict:
            args['definition'] = ProjectDefinitionResponse.from_dict(_dict.get('definition'))
        if 'configs' in _dict:
            args['configs'] = [ProjectConfigCollectionMember.from_dict(v) for v in _dict.get('configs')]
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
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
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
    The metadata of the project.

    :attr str crn: An IBM Cloud resource name, which uniquely identifies a resource.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr List[CumulativeNeedsAttention] cumulative_needs_attention_view: (optional)
          The cumulative list of needs attention items for a project. If the view is
          successfully retrieved, an array which could be empty is returned.
    :attr bool cumulative_needs_attention_view_error: (optional) True indicates that
          the fetch of the needs attention items failed. It only exists if there was an
          error while retrieving the cumulative needs attention view.
    :attr str id: (optional) The unique ID of a project.
    :attr str location: The IBM Cloud location where a resource is deployed.
    :attr str resource_group: The resource group where the project's data and tools
          are created.
    :attr str state: The project status value.
    :attr str event_notifications_crn: (optional) The CRN of the event notifications
          instance if one is connected to this project.
    :attr ProjectDefinitionResponse definition: (optional) The definition of the
          project.
    """

    def __init__(
        self,
        crn: str,
        created_at: datetime,
        location: str,
        resource_group: str,
        state: str,
        *,
        cumulative_needs_attention_view: List['CumulativeNeedsAttention'] = None,
        cumulative_needs_attention_view_error: bool = None,
        id: str = None,
        event_notifications_crn: str = None,
        definition: 'ProjectDefinitionResponse' = None,
    ) -> None:
        """
        Initialize a ProjectCollectionMemberWithMetadata object.

        :param str crn: An IBM Cloud resource name, which uniquely identifies a
               resource.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param str location: The IBM Cloud location where a resource is deployed.
        :param str resource_group: The resource group where the project's data and
               tools are created.
        :param str state: The project status value.
        :param List[CumulativeNeedsAttention] cumulative_needs_attention_view:
               (optional) The cumulative list of needs attention items for a project. If
               the view is successfully retrieved, an array which could be empty is
               returned.
        :param bool cumulative_needs_attention_view_error: (optional) True
               indicates that the fetch of the needs attention items failed. It only
               exists if there was an error while retrieving the cumulative needs
               attention view.
        :param str id: (optional) The unique ID of a project.
        :param str event_notifications_crn: (optional) The CRN of the event
               notifications instance if one is connected to this project.
        :param ProjectDefinitionResponse definition: (optional) The definition of
               the project.
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
        else:
            raise ValueError('Required property \'crn\' not present in ProjectCollectionMemberWithMetadata JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProjectCollectionMemberWithMetadata JSON')
        if 'cumulative_needs_attention_view' in _dict:
            args['cumulative_needs_attention_view'] = [CumulativeNeedsAttention.from_dict(v) for v in _dict.get('cumulative_needs_attention_view')]
        if 'cumulative_needs_attention_view_error' in _dict:
            args['cumulative_needs_attention_view_error'] = _dict.get('cumulative_needs_attention_view_error')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        else:
            raise ValueError('Required property \'location\' not present in ProjectCollectionMemberWithMetadata JSON')
        if 'resource_group' in _dict:
            args['resource_group'] = _dict.get('resource_group')
        else:
            raise ValueError('Required property \'resource_group\' not present in ProjectCollectionMemberWithMetadata JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectCollectionMemberWithMetadata JSON')
        if 'event_notifications_crn' in _dict:
            args['event_notifications_crn'] = _dict.get('event_notifications_crn')
        if 'definition' in _dict:
            args['definition'] = ProjectDefinitionResponse.from_dict(_dict.get('definition'))
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

    :attr str id: (optional) The unique ID of a project.
    :attr str target_iam_id: (optional) The unique ID of a project.
    """

    def __init__(
        self,
        *,
        id: str = None,
        target_iam_id: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigAuthTrustedProfile object.

        :param str id: (optional) The unique ID of a project.
        :param str target_iam_id: (optional) The unique ID of a project.
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
    The configuration metadata.

    :attr str id: The ID of the configuration. If this parameter is empty, an ID is
          automatically created for the configuration.
    :attr str project_id: The unique ID of a project.
    :attr int version: The version of the configuration.
    :attr bool is_draft: The flag that indicates whether the version of the
          configuration is draft, or active.
    :attr List[object] needs_attention_state: (optional) The needs attention state
          of a configuration.
    :attr str state: The state of the configuration.
    :attr str pipeline_state: (optional) The pipeline state of the configuration. It
          only exists after the first configuration validation.
    :attr bool update_available: The flag that indicates whether a configuration
          update is available.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr datetime updated_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr ProjectConfigMetadataLastApproved last_approved: (optional) The last
          approved metadata of the configuration.
    :attr datetime last_save: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr ProjectConfigDraftSummary active_draft: (optional) The project
          configuration draft.
    :attr ProjectConfigDefinition definition: The project configuration definition.
    :attr str href: A relative URL.
    """

    def __init__(
        self,
        id: str,
        project_id: str,
        version: int,
        is_draft: bool,
        state: str,
        update_available: bool,
        created_at: datetime,
        updated_at: datetime,
        definition: 'ProjectConfigDefinition',
        href: str,
        *,
        needs_attention_state: List[object] = None,
        pipeline_state: str = None,
        last_approved: 'ProjectConfigMetadataLastApproved' = None,
        last_save: datetime = None,
        active_draft: 'ProjectConfigDraftSummary' = None,
    ) -> None:
        """
        Initialize a ProjectConfigCollectionMember object.

        :param str id: The ID of the configuration. If this parameter is empty, an
               ID is automatically created for the configuration.
        :param str project_id: The unique ID of a project.
        :param int version: The version of the configuration.
        :param bool is_draft: The flag that indicates whether the version of the
               configuration is draft, or active.
        :param str state: The state of the configuration.
        :param bool update_available: The flag that indicates whether a
               configuration update is available.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param datetime updated_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param ProjectConfigDefinition definition: The project configuration
               definition.
        :param str href: A relative URL.
        :param List[object] needs_attention_state: (optional) The needs attention
               state of a configuration.
        :param str pipeline_state: (optional) The pipeline state of the
               configuration. It only exists after the first configuration validation.
        :param ProjectConfigMetadataLastApproved last_approved: (optional) The last
               approved metadata of the configuration.
        :param datetime last_save: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param ProjectConfigDraftSummary active_draft: (optional) The project
               configuration draft.
        """
        self.id = id
        self.project_id = project_id
        self.version = version
        self.is_draft = is_draft
        self.needs_attention_state = needs_attention_state
        self.state = state
        self.pipeline_state = pipeline_state
        self.update_available = update_available
        self.created_at = created_at
        self.updated_at = updated_at
        self.last_approved = last_approved
        self.last_save = last_save
        self.active_draft = active_draft
        self.definition = definition
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigCollectionMember':
        """Initialize a ProjectConfigCollectionMember object from a json dictionary."""
        args = {}
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
        if 'pipeline_state' in _dict:
            args['pipeline_state'] = _dict.get('pipeline_state')
        if 'update_available' in _dict:
            args['update_available'] = _dict.get('update_available')
        else:
            raise ValueError('Required property \'update_available\' not present in ProjectConfigCollectionMember JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProjectConfigCollectionMember JSON')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        else:
            raise ValueError('Required property \'updated_at\' not present in ProjectConfigCollectionMember JSON')
        if 'last_approved' in _dict:
            args['last_approved'] = ProjectConfigMetadataLastApproved.from_dict(_dict.get('last_approved'))
        if 'last_save' in _dict:
            args['last_save'] = string_to_datetime(_dict.get('last_save'))
        if 'active_draft' in _dict:
            args['active_draft'] = ProjectConfigDraftSummary.from_dict(_dict.get('active_draft'))
        if 'definition' in _dict:
            args['definition'] = ProjectConfigDefinition.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in ProjectConfigCollectionMember JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ProjectConfigCollectionMember JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigCollectionMember object from a json dictionary."""
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
        if hasattr(self, 'pipeline_state') and self.pipeline_state is not None:
            _dict['pipeline_state'] = self.pipeline_state
        if hasattr(self, 'update_available') and self.update_available is not None:
            _dict['update_available'] = self.update_available
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'last_approved') and self.last_approved is not None:
            if isinstance(self.last_approved, dict):
                _dict['last_approved'] = self.last_approved
            else:
                _dict['last_approved'] = self.last_approved.to_dict()
        if hasattr(self, 'last_save') and self.last_save is not None:
            _dict['last_save'] = datetime_to_string(self.last_save)
        if hasattr(self, 'active_draft') and self.active_draft is not None:
            if isinstance(self.active_draft, dict):
                _dict['active_draft'] = self.active_draft
            else:
                _dict['active_draft'] = self.active_draft.to_dict()
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
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


class ProjectConfigComplianceProfile:
    """
    The profile required for compliance.

    :attr str id: (optional) The unique ID of a project.
    :attr str instance_id: (optional) The unique ID of a project.
    :attr str instance_location: (optional) The location of the compliance instance.
    :attr str attachment_id: (optional) The unique ID of a project.
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
        Initialize a ProjectConfigComplianceProfile object.

        :param str id: (optional) The unique ID of a project.
        :param str instance_id: (optional) The unique ID of a project.
        :param str instance_location: (optional) The location of the compliance
               instance.
        :param str attachment_id: (optional) The unique ID of a project.
        :param str profile_name: (optional) The name of the compliance profile.
        """
        self.id = id
        self.instance_id = instance_id
        self.instance_location = instance_location
        self.attachment_id = attachment_id
        self.profile_name = profile_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigComplianceProfile':
        """Initialize a ProjectConfigComplianceProfile object from a json dictionary."""
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
        """Initialize a ProjectConfigComplianceProfile object from a json dictionary."""
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
        """Return a `str` version of this ProjectConfigComplianceProfile object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigComplianceProfile') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigComplianceProfile') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigDefinition:
    """
    The project configuration definition.

    :attr str name: The name of the configuration.
    :attr List[str] labels: (optional) A collection of configuration labels.
    :attr str description: (optional) The description of the project configuration.
    :attr ProjectConfigAuth authorizations: (optional) The authorization for a
          configuration.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr ProjectConfigComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    :attr str locator_id: A dotted value of catalogID.versionID.
    :attr str type: The type of a project configuration manual property.
    :attr List[InputVariable] input: (optional) The outputs of a Schematics template
          property.
    :attr List[OutputValue] output: (optional) The outputs of a Schematics template
          property.
    :attr List[ProjectConfigSettingCollection] setting: (optional) Schematics
          environment variables to use to deploy the configuration. Settings are only
          available if they were specified when the configuration was initially created.
    """

    def __init__(
        self,
        name: str,
        locator_id: str,
        type: str,
        *,
        labels: List[str] = None,
        description: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        compliance_profile: 'ProjectConfigComplianceProfile' = None,
        input: List['InputVariable'] = None,
        output: List['OutputValue'] = None,
        setting: List['ProjectConfigSettingCollection'] = None,
    ) -> None:
        """
        Initialize a ProjectConfigDefinition object.

        :param str name: The name of the configuration.
        :param str locator_id: A dotted value of catalogID.versionID.
        :param str type: The type of a project configuration manual property.
        :param List[str] labels: (optional) A collection of configuration labels.
        :param str description: (optional) The description of the project
               configuration.
        :param ProjectConfigAuth authorizations: (optional) The authorization for a
               configuration.
               You can authorize by using a trusted profile or an API key in Secrets
               Manager.
        :param ProjectConfigComplianceProfile compliance_profile: (optional) The
               profile required for compliance.
        :param List[InputVariable] input: (optional) The outputs of a Schematics
               template property.
        :param List[OutputValue] output: (optional) The outputs of a Schematics
               template property.
        :param List[ProjectConfigSettingCollection] setting: (optional) Schematics
               environment variables to use to deploy the configuration. Settings are only
               available if they were specified when the configuration was initially
               created.
        """
        self.name = name
        self.labels = labels
        self.description = description
        self.authorizations = authorizations
        self.compliance_profile = compliance_profile
        self.locator_id = locator_id
        self.type = type
        self.input = input
        self.output = output
        self.setting = setting

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigDefinition':
        """Initialize a ProjectConfigDefinition object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ProjectConfigDefinition JSON')
        if 'labels' in _dict:
            args['labels'] = _dict.get('labels')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'compliance_profile' in _dict:
            args['compliance_profile'] = ProjectConfigComplianceProfile.from_dict(_dict.get('compliance_profile'))
        if 'locator_id' in _dict:
            args['locator_id'] = _dict.get('locator_id')
        else:
            raise ValueError('Required property \'locator_id\' not present in ProjectConfigDefinition JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in ProjectConfigDefinition JSON')
        if 'input' in _dict:
            args['input'] = [InputVariable.from_dict(v) for v in _dict.get('input')]
        if 'output' in _dict:
            args['output'] = [OutputValue.from_dict(v) for v in _dict.get('output')]
        if 'setting' in _dict:
            args['setting'] = [ProjectConfigSettingCollection.from_dict(v) for v in _dict.get('setting')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigDefinition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
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
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'input') and self.input is not None:
            input_list = []
            for v in self.input:
                if isinstance(v, dict):
                    input_list.append(v)
                else:
                    input_list.append(v.to_dict())
            _dict['input'] = input_list
        if hasattr(self, 'output') and self.output is not None:
            output_list = []
            for v in self.output:
                if isinstance(v, dict):
                    output_list.append(v)
                else:
                    output_list.append(v.to_dict())
            _dict['output'] = output_list
        if hasattr(self, 'setting') and self.setting is not None:
            setting_list = []
            for v in self.setting:
                if isinstance(v, dict):
                    setting_list.append(v)
                else:
                    setting_list.append(v.to_dict())
            _dict['setting'] = setting_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigDefinition object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigDefinition') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigDefinition') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of a project configuration manual property.
        """

        TERRAFORM_TEMPLATE = 'terraform_template'
        SCHEMATICS_BLUEPRINT = 'schematics_blueprint'



class ProjectConfigDelete:
    """
    Deletes the configuration response.

    :attr str id: The unique ID of a project.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a ProjectConfigDelete object.

        :param str id: The unique ID of a project.
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


class ProjectConfigDraftResponse:
    """
    The project configuration draft.

    :attr str id: The ID of the configuration. If this parameter is empty, an ID is
          automatically created for the configuration.
    :attr str project_id: The unique ID of a project.
    :attr int version: The version of the configuration.
    :attr bool is_draft: The flag that indicates whether the version of the
          configuration is draft, or active.
    :attr List[object] needs_attention_state: (optional) The needs attention state
          of a configuration.
    :attr str state: The state of the configuration.
    :attr str pipeline_state: (optional) The pipeline state of the configuration. It
          only exists after the first configuration validation.
    :attr bool update_available: The flag that indicates whether a configuration
          update is available.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr datetime updated_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr ProjectConfigMetadataLastApproved last_approved: (optional) The last
          approved metadata of the configuration.
    :attr datetime last_save: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr ProjectConfigMetadataJobSummary job_summary: (optional) The summaries of
          jobs that were performed on the configuration.
    :attr ProjectConfigMetadataCraLogs cra_logs: (optional) The Code Risk Analyzer
          logs of the configuration.
    :attr ProjectConfigMetadataCostEstimate cost_estimate: (optional) The cost
          estimate of the configuration.
          It only exists after the first configuration validation.
    :attr ProjectConfigMetadataJobSummary last_deployment_job_summary: (optional)
          The summaries of jobs that were performed on the configuration.
    :attr ProjectConfigDefinition definition: The project configuration definition.
    """

    def __init__(
        self,
        id: str,
        project_id: str,
        version: int,
        is_draft: bool,
        state: str,
        update_available: bool,
        created_at: datetime,
        updated_at: datetime,
        definition: 'ProjectConfigDefinition',
        *,
        needs_attention_state: List[object] = None,
        pipeline_state: str = None,
        last_approved: 'ProjectConfigMetadataLastApproved' = None,
        last_save: datetime = None,
        job_summary: 'ProjectConfigMetadataJobSummary' = None,
        cra_logs: 'ProjectConfigMetadataCraLogs' = None,
        cost_estimate: 'ProjectConfigMetadataCostEstimate' = None,
        last_deployment_job_summary: 'ProjectConfigMetadataJobSummary' = None,
    ) -> None:
        """
        Initialize a ProjectConfigDraftResponse object.

        :param str id: The ID of the configuration. If this parameter is empty, an
               ID is automatically created for the configuration.
        :param str project_id: The unique ID of a project.
        :param int version: The version of the configuration.
        :param bool is_draft: The flag that indicates whether the version of the
               configuration is draft, or active.
        :param str state: The state of the configuration.
        :param bool update_available: The flag that indicates whether a
               configuration update is available.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param datetime updated_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param ProjectConfigDefinition definition: The project configuration
               definition.
        :param List[object] needs_attention_state: (optional) The needs attention
               state of a configuration.
        :param str pipeline_state: (optional) The pipeline state of the
               configuration. It only exists after the first configuration validation.
        :param ProjectConfigMetadataLastApproved last_approved: (optional) The last
               approved metadata of the configuration.
        :param datetime last_save: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param ProjectConfigMetadataJobSummary job_summary: (optional) The
               summaries of jobs that were performed on the configuration.
        :param ProjectConfigMetadataCraLogs cra_logs: (optional) The Code Risk
               Analyzer logs of the configuration.
        :param ProjectConfigMetadataCostEstimate cost_estimate: (optional) The cost
               estimate of the configuration.
               It only exists after the first configuration validation.
        :param ProjectConfigMetadataJobSummary last_deployment_job_summary:
               (optional) The summaries of jobs that were performed on the configuration.
        """
        self.id = id
        self.project_id = project_id
        self.version = version
        self.is_draft = is_draft
        self.needs_attention_state = needs_attention_state
        self.state = state
        self.pipeline_state = pipeline_state
        self.update_available = update_available
        self.created_at = created_at
        self.updated_at = updated_at
        self.last_approved = last_approved
        self.last_save = last_save
        self.job_summary = job_summary
        self.cra_logs = cra_logs
        self.cost_estimate = cost_estimate
        self.last_deployment_job_summary = last_deployment_job_summary
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigDraftResponse':
        """Initialize a ProjectConfigDraftResponse object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectConfigDraftResponse JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in ProjectConfigDraftResponse JSON')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in ProjectConfigDraftResponse JSON')
        if 'is_draft' in _dict:
            args['is_draft'] = _dict.get('is_draft')
        else:
            raise ValueError('Required property \'is_draft\' not present in ProjectConfigDraftResponse JSON')
        if 'needs_attention_state' in _dict:
            args['needs_attention_state'] = _dict.get('needs_attention_state')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectConfigDraftResponse JSON')
        if 'pipeline_state' in _dict:
            args['pipeline_state'] = _dict.get('pipeline_state')
        if 'update_available' in _dict:
            args['update_available'] = _dict.get('update_available')
        else:
            raise ValueError('Required property \'update_available\' not present in ProjectConfigDraftResponse JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProjectConfigDraftResponse JSON')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        else:
            raise ValueError('Required property \'updated_at\' not present in ProjectConfigDraftResponse JSON')
        if 'last_approved' in _dict:
            args['last_approved'] = ProjectConfigMetadataLastApproved.from_dict(_dict.get('last_approved'))
        if 'last_save' in _dict:
            args['last_save'] = string_to_datetime(_dict.get('last_save'))
        if 'job_summary' in _dict:
            args['job_summary'] = ProjectConfigMetadataJobSummary.from_dict(_dict.get('job_summary'))
        if 'cra_logs' in _dict:
            args['cra_logs'] = ProjectConfigMetadataCraLogs.from_dict(_dict.get('cra_logs'))
        if 'cost_estimate' in _dict:
            args['cost_estimate'] = ProjectConfigMetadataCostEstimate.from_dict(_dict.get('cost_estimate'))
        if 'last_deployment_job_summary' in _dict:
            args['last_deployment_job_summary'] = ProjectConfigMetadataJobSummary.from_dict(_dict.get('last_deployment_job_summary'))
        if 'definition' in _dict:
            args['definition'] = ProjectConfigDefinition.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in ProjectConfigDraftResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigDraftResponse object from a json dictionary."""
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
        if hasattr(self, 'pipeline_state') and self.pipeline_state is not None:
            _dict['pipeline_state'] = self.pipeline_state
        if hasattr(self, 'update_available') and self.update_available is not None:
            _dict['update_available'] = self.update_available
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'last_approved') and self.last_approved is not None:
            if isinstance(self.last_approved, dict):
                _dict['last_approved'] = self.last_approved
            else:
                _dict['last_approved'] = self.last_approved.to_dict()
        if hasattr(self, 'last_save') and self.last_save is not None:
            _dict['last_save'] = datetime_to_string(self.last_save)
        if hasattr(self, 'job_summary') and self.job_summary is not None:
            if isinstance(self.job_summary, dict):
                _dict['job_summary'] = self.job_summary
            else:
                _dict['job_summary'] = self.job_summary.to_dict()
        if hasattr(self, 'cra_logs') and self.cra_logs is not None:
            if isinstance(self.cra_logs, dict):
                _dict['cra_logs'] = self.cra_logs
            else:
                _dict['cra_logs'] = self.cra_logs.to_dict()
        if hasattr(self, 'cost_estimate') and self.cost_estimate is not None:
            if isinstance(self.cost_estimate, dict):
                _dict['cost_estimate'] = self.cost_estimate
            else:
                _dict['cost_estimate'] = self.cost_estimate.to_dict()
        if hasattr(self, 'last_deployment_job_summary') and self.last_deployment_job_summary is not None:
            if isinstance(self.last_deployment_job_summary, dict):
                _dict['last_deployment_job_summary'] = self.last_deployment_job_summary
            else:
                _dict['last_deployment_job_summary'] = self.last_deployment_job_summary.to_dict()
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
        """Return a `str` version of this ProjectConfigDraftResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigDraftResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigDraftResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigDraftSummary:
    """
    The project configuration draft.

    :attr int version: The version number of the configuration.
    :attr str state: The state of the configuration draft.
    :attr str pipeline_state: (optional) The pipeline state of the configuration. It
          only exists after the first configuration validation.
    :attr str href: (optional) A relative URL.
    """

    def __init__(
        self,
        version: int,
        state: str,
        *,
        pipeline_state: str = None,
        href: str = None,
    ) -> None:
        """
        Initialize a ProjectConfigDraftSummary object.

        :param int version: The version number of the configuration.
        :param str state: The state of the configuration draft.
        :param str pipeline_state: (optional) The pipeline state of the
               configuration. It only exists after the first configuration validation.
        :param str href: (optional) A relative URL.
        """
        self.version = version
        self.state = state
        self.pipeline_state = pipeline_state
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigDraftSummary':
        """Initialize a ProjectConfigDraftSummary object from a json dictionary."""
        args = {}
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in ProjectConfigDraftSummary JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectConfigDraftSummary JSON')
        if 'pipeline_state' in _dict:
            args['pipeline_state'] = _dict.get('pipeline_state')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigDraftSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'pipeline_state') and self.pipeline_state is not None:
            _dict['pipeline_state'] = self.pipeline_state
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigDraftSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigDraftSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigDraftSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigDraftSummaryCollection:
    """
    The project configuration draft list.

    :attr List[ProjectConfigDraftSummary] drafts: (optional) The collection list
          operation response schema that defines the array property with the name
          `drafts`.
    """

    def __init__(
        self,
        *,
        drafts: List['ProjectConfigDraftSummary'] = None,
    ) -> None:
        """
        Initialize a ProjectConfigDraftSummaryCollection object.

        :param List[ProjectConfigDraftSummary] drafts: (optional) The collection
               list operation response schema that defines the array property with the
               name `drafts`.
        """
        self.drafts = drafts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigDraftSummaryCollection':
        """Initialize a ProjectConfigDraftSummaryCollection object from a json dictionary."""
        args = {}
        if 'drafts' in _dict:
            args['drafts'] = [ProjectConfigDraftSummary.from_dict(v) for v in _dict.get('drafts')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigDraftSummaryCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'drafts') and self.drafts is not None:
            drafts_list = []
            for v in self.drafts:
                if isinstance(v, dict):
                    drafts_list.append(v)
                else:
                    drafts_list.append(v.to_dict())
            _dict['drafts'] = drafts_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigDraftSummaryCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigDraftSummaryCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigDraftSummaryCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigGetResponse:
    """
    The configuration metadata.

    :attr str id: The ID of the configuration. If this parameter is empty, an ID is
          automatically created for the configuration.
    :attr str project_id: The unique ID of a project.
    :attr int version: The version of the configuration.
    :attr bool is_draft: The flag that indicates whether the version of the
          configuration is draft, or active.
    :attr List[object] needs_attention_state: (optional) The needs attention state
          of a configuration.
    :attr str state: The state of the configuration.
    :attr str pipeline_state: (optional) The pipeline state of the configuration. It
          only exists after the first configuration validation.
    :attr bool update_available: The flag that indicates whether a configuration
          update is available.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr datetime updated_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr ProjectConfigMetadataLastApproved last_approved: (optional) The last
          approved metadata of the configuration.
    :attr datetime last_save: (optional) A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr ProjectConfigMetadataJobSummary job_summary: (optional) The summaries of
          jobs that were performed on the configuration.
    :attr ProjectConfigMetadataCraLogs cra_logs: (optional) The Code Risk Analyzer
          logs of the configuration.
    :attr ProjectConfigMetadataCostEstimate cost_estimate: (optional) The cost
          estimate of the configuration.
          It only exists after the first configuration validation.
    :attr ProjectConfigMetadataJobSummary last_deployment_job_summary: (optional)
          The summaries of jobs that were performed on the configuration.
    :attr ProjectConfigDraftSummary active_draft: (optional) The project
          configuration draft.
    :attr ProjectConfigDefinition definition: The project configuration definition.
    """

    def __init__(
        self,
        id: str,
        project_id: str,
        version: int,
        is_draft: bool,
        state: str,
        update_available: bool,
        created_at: datetime,
        updated_at: datetime,
        definition: 'ProjectConfigDefinition',
        *,
        needs_attention_state: List[object] = None,
        pipeline_state: str = None,
        last_approved: 'ProjectConfigMetadataLastApproved' = None,
        last_save: datetime = None,
        job_summary: 'ProjectConfigMetadataJobSummary' = None,
        cra_logs: 'ProjectConfigMetadataCraLogs' = None,
        cost_estimate: 'ProjectConfigMetadataCostEstimate' = None,
        last_deployment_job_summary: 'ProjectConfigMetadataJobSummary' = None,
        active_draft: 'ProjectConfigDraftSummary' = None,
    ) -> None:
        """
        Initialize a ProjectConfigGetResponse object.

        :param str id: The ID of the configuration. If this parameter is empty, an
               ID is automatically created for the configuration.
        :param str project_id: The unique ID of a project.
        :param int version: The version of the configuration.
        :param bool is_draft: The flag that indicates whether the version of the
               configuration is draft, or active.
        :param str state: The state of the configuration.
        :param bool update_available: The flag that indicates whether a
               configuration update is available.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param datetime updated_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param ProjectConfigDefinition definition: The project configuration
               definition.
        :param List[object] needs_attention_state: (optional) The needs attention
               state of a configuration.
        :param str pipeline_state: (optional) The pipeline state of the
               configuration. It only exists after the first configuration validation.
        :param ProjectConfigMetadataLastApproved last_approved: (optional) The last
               approved metadata of the configuration.
        :param datetime last_save: (optional) A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param ProjectConfigMetadataJobSummary job_summary: (optional) The
               summaries of jobs that were performed on the configuration.
        :param ProjectConfigMetadataCraLogs cra_logs: (optional) The Code Risk
               Analyzer logs of the configuration.
        :param ProjectConfigMetadataCostEstimate cost_estimate: (optional) The cost
               estimate of the configuration.
               It only exists after the first configuration validation.
        :param ProjectConfigMetadataJobSummary last_deployment_job_summary:
               (optional) The summaries of jobs that were performed on the configuration.
        :param ProjectConfigDraftSummary active_draft: (optional) The project
               configuration draft.
        """
        self.id = id
        self.project_id = project_id
        self.version = version
        self.is_draft = is_draft
        self.needs_attention_state = needs_attention_state
        self.state = state
        self.pipeline_state = pipeline_state
        self.update_available = update_available
        self.created_at = created_at
        self.updated_at = updated_at
        self.last_approved = last_approved
        self.last_save = last_save
        self.job_summary = job_summary
        self.cra_logs = cra_logs
        self.cost_estimate = cost_estimate
        self.last_deployment_job_summary = last_deployment_job_summary
        self.active_draft = active_draft
        self.definition = definition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigGetResponse':
        """Initialize a ProjectConfigGetResponse object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ProjectConfigGetResponse JSON')
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError('Required property \'project_id\' not present in ProjectConfigGetResponse JSON')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in ProjectConfigGetResponse JSON')
        if 'is_draft' in _dict:
            args['is_draft'] = _dict.get('is_draft')
        else:
            raise ValueError('Required property \'is_draft\' not present in ProjectConfigGetResponse JSON')
        if 'needs_attention_state' in _dict:
            args['needs_attention_state'] = _dict.get('needs_attention_state')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectConfigGetResponse JSON')
        if 'pipeline_state' in _dict:
            args['pipeline_state'] = _dict.get('pipeline_state')
        if 'update_available' in _dict:
            args['update_available'] = _dict.get('update_available')
        else:
            raise ValueError('Required property \'update_available\' not present in ProjectConfigGetResponse JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ProjectConfigGetResponse JSON')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        else:
            raise ValueError('Required property \'updated_at\' not present in ProjectConfigGetResponse JSON')
        if 'last_approved' in _dict:
            args['last_approved'] = ProjectConfigMetadataLastApproved.from_dict(_dict.get('last_approved'))
        if 'last_save' in _dict:
            args['last_save'] = string_to_datetime(_dict.get('last_save'))
        if 'job_summary' in _dict:
            args['job_summary'] = ProjectConfigMetadataJobSummary.from_dict(_dict.get('job_summary'))
        if 'cra_logs' in _dict:
            args['cra_logs'] = ProjectConfigMetadataCraLogs.from_dict(_dict.get('cra_logs'))
        if 'cost_estimate' in _dict:
            args['cost_estimate'] = ProjectConfigMetadataCostEstimate.from_dict(_dict.get('cost_estimate'))
        if 'last_deployment_job_summary' in _dict:
            args['last_deployment_job_summary'] = ProjectConfigMetadataJobSummary.from_dict(_dict.get('last_deployment_job_summary'))
        if 'active_draft' in _dict:
            args['active_draft'] = ProjectConfigDraftSummary.from_dict(_dict.get('active_draft'))
        if 'definition' in _dict:
            args['definition'] = ProjectConfigDefinition.from_dict(_dict.get('definition'))
        else:
            raise ValueError('Required property \'definition\' not present in ProjectConfigGetResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigGetResponse object from a json dictionary."""
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
        if hasattr(self, 'pipeline_state') and self.pipeline_state is not None:
            _dict['pipeline_state'] = self.pipeline_state
        if hasattr(self, 'update_available') and self.update_available is not None:
            _dict['update_available'] = self.update_available
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'last_approved') and self.last_approved is not None:
            if isinstance(self.last_approved, dict):
                _dict['last_approved'] = self.last_approved
            else:
                _dict['last_approved'] = self.last_approved.to_dict()
        if hasattr(self, 'last_save') and self.last_save is not None:
            _dict['last_save'] = datetime_to_string(self.last_save)
        if hasattr(self, 'job_summary') and self.job_summary is not None:
            if isinstance(self.job_summary, dict):
                _dict['job_summary'] = self.job_summary
            else:
                _dict['job_summary'] = self.job_summary.to_dict()
        if hasattr(self, 'cra_logs') and self.cra_logs is not None:
            if isinstance(self.cra_logs, dict):
                _dict['cra_logs'] = self.cra_logs
            else:
                _dict['cra_logs'] = self.cra_logs.to_dict()
        if hasattr(self, 'cost_estimate') and self.cost_estimate is not None:
            if isinstance(self.cost_estimate, dict):
                _dict['cost_estimate'] = self.cost_estimate
            else:
                _dict['cost_estimate'] = self.cost_estimate.to_dict()
        if hasattr(self, 'last_deployment_job_summary') and self.last_deployment_job_summary is not None:
            if isinstance(self.last_deployment_job_summary, dict):
                _dict['last_deployment_job_summary'] = self.last_deployment_job_summary
            else:
                _dict['last_deployment_job_summary'] = self.last_deployment_job_summary.to_dict()
        if hasattr(self, 'active_draft') and self.active_draft is not None:
            if isinstance(self.active_draft, dict):
                _dict['active_draft'] = self.active_draft
            else:
                _dict['active_draft'] = self.active_draft.to_dict()
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
        """Return a `str` version of this ProjectConfigGetResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigGetResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigGetResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectConfigInputVariable:
    """
    ProjectConfigInputVariable.

    :attr str name: The variable name.
    :attr object value: (optional) Can be any value - a string, number, boolean,
          array, or object.
    """

    def __init__(
        self,
        name: str,
        *,
        value: object = None,
    ) -> None:
        """
        Initialize a ProjectConfigInputVariable object.

        :param str name: The variable name.
        :param object value: (optional) Can be any value - a string, number,
               boolean, array, or object.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigInputVariable':
        """Initialize a ProjectConfigInputVariable object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ProjectConfigInputVariable JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigInputVariable object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigInputVariable object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigInputVariable') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigInputVariable') -> bool:
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
    :attr str user_id: (optional) The unique ID of a project.
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
        :param str user_id: (optional) The unique ID of a project.
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


class ProjectConfigMetadataJobSummary:
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
        Initialize a ProjectConfigMetadataJobSummary object.

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
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigMetadataJobSummary':
        """Initialize a ProjectConfigMetadataJobSummary object from a json dictionary."""
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
        """Initialize a ProjectConfigMetadataJobSummary object from a json dictionary."""
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
        """Return a `str` version of this ProjectConfigMetadataJobSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigMetadataJobSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigMetadataJobSummary') -> bool:
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
    :attr str user_id: The unique ID of a project.
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
        :param str user_id: The unique ID of a project.
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

    :attr str name: The name of the configuration.
    :attr List[str] labels: (optional) A collection of configuration labels.
    :attr str description: (optional) The description of the project configuration.
    :attr ProjectConfigAuth authorizations: (optional) The authorization for a
          configuration.
          You can authorize by using a trusted profile or an API key in Secrets Manager.
    :attr ProjectConfigComplianceProfile compliance_profile: (optional) The profile
          required for compliance.
    :attr str locator_id: A dotted value of catalogID.versionID.
    :attr List[ProjectConfigInputVariable] input: (optional) The inputs of a
          Schematics template property.
    :attr List[ProjectConfigSettingCollection] setting: (optional) Schematics
          environment variables to use to deploy the configuration. Settings are only
          available if they were specified when the configuration was initially created.
    """

    def __init__(
        self,
        name: str,
        locator_id: str,
        *,
        labels: List[str] = None,
        description: str = None,
        authorizations: 'ProjectConfigAuth' = None,
        compliance_profile: 'ProjectConfigComplianceProfile' = None,
        input: List['ProjectConfigInputVariable'] = None,
        setting: List['ProjectConfigSettingCollection'] = None,
    ) -> None:
        """
        Initialize a ProjectConfigPrototype object.

        :param str name: The name of the configuration.
        :param str locator_id: A dotted value of catalogID.versionID.
        :param List[str] labels: (optional) A collection of configuration labels.
        :param str description: (optional) The description of the project
               configuration.
        :param ProjectConfigAuth authorizations: (optional) The authorization for a
               configuration.
               You can authorize by using a trusted profile or an API key in Secrets
               Manager.
        :param ProjectConfigComplianceProfile compliance_profile: (optional) The
               profile required for compliance.
        :param List[ProjectConfigInputVariable] input: (optional) The inputs of a
               Schematics template property.
        :param List[ProjectConfigSettingCollection] setting: (optional) Schematics
               environment variables to use to deploy the configuration. Settings are only
               available if they were specified when the configuration was initially
               created.
        """
        self.name = name
        self.labels = labels
        self.description = description
        self.authorizations = authorizations
        self.compliance_profile = compliance_profile
        self.locator_id = locator_id
        self.input = input
        self.setting = setting

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigPrototype':
        """Initialize a ProjectConfigPrototype object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ProjectConfigPrototype JSON')
        if 'labels' in _dict:
            args['labels'] = _dict.get('labels')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'authorizations' in _dict:
            args['authorizations'] = ProjectConfigAuth.from_dict(_dict.get('authorizations'))
        if 'compliance_profile' in _dict:
            args['compliance_profile'] = ProjectConfigComplianceProfile.from_dict(_dict.get('compliance_profile'))
        if 'locator_id' in _dict:
            args['locator_id'] = _dict.get('locator_id')
        else:
            raise ValueError('Required property \'locator_id\' not present in ProjectConfigPrototype JSON')
        if 'input' in _dict:
            args['input'] = [ProjectConfigInputVariable.from_dict(v) for v in _dict.get('input')]
        if 'setting' in _dict:
            args['setting'] = [ProjectConfigSettingCollection.from_dict(v) for v in _dict.get('setting')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigPrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'labels') and self.labels is not None:
            _dict['labels'] = self.labels
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
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
            input_list = []
            for v in self.input:
                if isinstance(v, dict):
                    input_list.append(v)
                else:
                    input_list.append(v.to_dict())
            _dict['input'] = input_list
        if hasattr(self, 'setting') and self.setting is not None:
            setting_list = []
            for v in self.setting:
                if isinstance(v, dict):
                    setting_list.append(v)
                else:
                    setting_list.append(v.to_dict())
            _dict['setting'] = setting_list
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


class ProjectConfigSettingCollection:
    """
    ProjectConfigSettingCollection.

    :attr str name: The name of the configuration setting.
    :attr str value: The value of the configuration setting.
    """

    def __init__(
        self,
        name: str,
        value: str,
    ) -> None:
        """
        Initialize a ProjectConfigSettingCollection object.

        :param str name: The name of the configuration setting.
        :param str value: The value of the configuration setting.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectConfigSettingCollection':
        """Initialize a ProjectConfigSettingCollection object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ProjectConfigSettingCollection JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ProjectConfigSettingCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectConfigSettingCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProjectConfigSettingCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectConfigSettingCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectConfigSettingCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectDefinitionResponse:
    """
    The definition of the project.

    :attr str name: The name of the project.
    :attr str description: A brief explanation of the project's use in the
          configuration of a deployable architecture. It is possible to create a project
          without providing a description.
    :attr bool destroy_on_delete: The policy that indicates whether the resources
          are destroyed or not when a project is deleted.
    """

    def __init__(
        self,
        name: str,
        description: str,
        destroy_on_delete: bool,
    ) -> None:
        """
        Initialize a ProjectDefinitionResponse object.

        :param str name: The name of the project.
        :param str description: A brief explanation of the project's use in the
               configuration of a deployable architecture. It is possible to create a
               project without providing a description.
        :param bool destroy_on_delete: The policy that indicates whether the
               resources are destroyed or not when a project is deleted.
        """
        self.name = name
        self.description = description
        self.destroy_on_delete = destroy_on_delete

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProjectDefinitionResponse':
        """Initialize a ProjectDefinitionResponse object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ProjectDefinitionResponse JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in ProjectDefinitionResponse JSON')
        if 'destroy_on_delete' in _dict:
            args['destroy_on_delete'] = _dict.get('destroy_on_delete')
        else:
            raise ValueError('Required property \'destroy_on_delete\' not present in ProjectDefinitionResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProjectDefinitionResponse object from a json dictionary."""
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
        """Return a `str` version of this ProjectDefinitionResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProjectDefinitionResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProjectDefinitionResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProjectSummary:
    """
    The project returned in the response body.

    :attr str crn: An IBM Cloud resource name, which uniquely identifies a resource.
    :attr datetime created_at: A date and time value in the format
          YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and time
          format as specified by RFC 3339.
    :attr List[CumulativeNeedsAttention] cumulative_needs_attention_view: (optional)
          The cumulative list of needs attention items for a project. If the view is
          successfully retrieved, an array which could be empty is returned.
    :attr bool cumulative_needs_attention_view_error: (optional) True indicates that
          the fetch of the needs attention items failed. It only exists if there was an
          error while retrieving the cumulative needs attention view.
    :attr str id: (optional) The unique ID of a project.
    :attr str location: The IBM Cloud location where a resource is deployed.
    :attr str resource_group: The resource group where the project's data and tools
          are created.
    :attr str state: The project status value.
    :attr str event_notifications_crn: (optional) The CRN of the event notifications
          instance if one is connected to this project.
    :attr ProjectDefinitionResponse definition: (optional) The definition of the
          project.
    """

    def __init__(
        self,
        crn: str,
        created_at: datetime,
        location: str,
        resource_group: str,
        state: str,
        *,
        cumulative_needs_attention_view: List['CumulativeNeedsAttention'] = None,
        cumulative_needs_attention_view_error: bool = None,
        id: str = None,
        event_notifications_crn: str = None,
        definition: 'ProjectDefinitionResponse' = None,
    ) -> None:
        """
        Initialize a ProjectSummary object.

        :param str crn: An IBM Cloud resource name, which uniquely identifies a
               resource.
        :param datetime created_at: A date and time value in the format
               YYYY-MM-DDTHH:mm:ssZ or YYYY-MM-DDTHH:mm:ss.sssZ, matching the date and
               time format as specified by RFC 3339.
        :param str location: The IBM Cloud location where a resource is deployed.
        :param str resource_group: The resource group where the project's data and
               tools are created.
        :param str state: The project status value.
        :param List[CumulativeNeedsAttention] cumulative_needs_attention_view:
               (optional) The cumulative list of needs attention items for a project. If
               the view is successfully retrieved, an array which could be empty is
               returned.
        :param bool cumulative_needs_attention_view_error: (optional) True
               indicates that the fetch of the needs attention items failed. It only
               exists if there was an error while retrieving the cumulative needs
               attention view.
        :param str id: (optional) The unique ID of a project.
        :param str event_notifications_crn: (optional) The CRN of the event
               notifications instance if one is connected to this project.
        :param ProjectDefinitionResponse definition: (optional) The definition of
               the project.
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
            args['cumulative_needs_attention_view'] = [CumulativeNeedsAttention.from_dict(v) for v in _dict.get('cumulative_needs_attention_view')]
        if 'cumulative_needs_attention_view_error' in _dict:
            args['cumulative_needs_attention_view_error'] = _dict.get('cumulative_needs_attention_view_error')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        else:
            raise ValueError('Required property \'location\' not present in ProjectSummary JSON')
        if 'resource_group' in _dict:
            args['resource_group'] = _dict.get('resource_group')
        else:
            raise ValueError('Required property \'resource_group\' not present in ProjectSummary JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ProjectSummary JSON')
        if 'event_notifications_crn' in _dict:
            args['event_notifications_crn'] = _dict.get('event_notifications_crn')
        if 'definition' in _dict:
            args['definition'] = ProjectDefinitionResponse.from_dict(_dict.get('definition'))
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
            next = next_page_link.get('start')
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
