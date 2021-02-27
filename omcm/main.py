import logging

from omc.core import console
from omc.service import omc_service

import omcm
from omcm.main_app import App
from omcm.service.omcm_service import OmcResourceAction


def main():
    omcm = App()
    omcm.run()


if __name__ == '__main__':

    # action = OmcResourceAction(omc_service.exec('omc smax cd150 namespace'.split(), True))
    # console.log(action.get_commands())
    main()
    # the_method = omc_service.exec(['omc', 'smax', 'cd219', 'namespace'], True)
    # print(the_method)
