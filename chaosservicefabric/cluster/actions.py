# -*- coding: utf-8 -*-
import json
import logging
from typing import Any, Dict

import requests
from chaoslib.exceptions import FailedActivity
from chaoslib.types import Configuration, Secrets

from chaosservicefabric import auth
from chaosservicefabric.types import ChaosParameters

__all__ = ["start_chaos", "stop_chaos"]
logger = logging.getLogger("chaostoolkit")


def start_chaos(
    parameters: ChaosParameters,
    timeout: int = 60,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> Dict[str, Any]:
    """
    Start Chaos in your cluster using the given `parameters`. This is a mapping
    of keys as declared in the Service Fabric API:

    https://docs.microsoft.com/en-us/rest/api/servicefabric/sfclient-model-chaosparameters

    Please see the :func:`chaosservicefabric.fabric.auth` help for more
    information on authenticating with the service.
    """  # noqa: E501
    with auth(configuration, secrets) as info:
        url = "{}/Tools/Chaos/$/Start".format(info["endpoint"])

        qs = {"api-version": "6.0"}
        if timeout is not None:
            qs["timeout"] = timeout

        r = requests.post(
            url,
            headers={"Accept": "application/json"},
            verify=info["verify"],
            params=qs,
            json=parameters,
        )

        if r.status_code != 200:
            error = r.json()
            raise FailedActivity(
                "Service Fabric Chaos failed to start: {}".format(
                    json.dumps(error)
                )
            )

        logger.debug("chaos started succesfully")

        return r.json()


def stop_chaos(
    timeout: int = 60,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> Dict[str, Any]:
    """
    Stop Chaos in your cluster.

    Please see the :func:`chaosservicefabric.fabric.auth` help for more
    information on authenticating with the service.
    """
    with auth(configuration, secrets) as info:
        url = "{}/Tools/Chaos/$/Stop".format(info["endpoint"])

        qs = {"api-version": "6.0"}
        if timeout is not None:
            qs["timeout"] = timeout

        r = requests.post(
            url,
            headers={"Accept": "application/json"},
            verify=info["verify"],
            params=qs,
        )

        if r.status_code != 200:
            error = r.json()
            raise FailedActivity(
                "Service Fabric Chaos failed to stop: {}".format(
                    json.dumps(error)
                )
            )

        logger.debug("chaos stopped succesfully")

        return r.json()
