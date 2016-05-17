# -*- coding: utf-8 -*-
"""
    lantz.drivers.stanford.sg396
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Implementation of SG396 signal generator

    Author: Kevin Miao
    Date: 12/15/2015
"""

import numpy as np
from lantz import Action, Feat, DictFeat, ureg
from lantz.messagebased import MessageBasedDriver

class SG396(MessageBasedDriver):

        DEFAULTS = {
            'COMMON': {
                'write_termination': '\r\n',
                'read_termination': '\r\n',
            }
        }

        # Signal synthesis commands

        @Feat
        def lf_amplitude(self):
            """
            low frequency amplitude (BNC output)
            """
            return self.query('AMPL?')

        @lf_amplitude.setter
        def lf_amplitude(self, value):
            self.write('AMPL{:.2f}'.format(value))

        @Feat
        def rf_amplitude(self):
            """
            RF amplitude (Type N output)
            """
            return self.query('AMPR?')

        @rf_amplitude.setter
        def rf_amplitude(self, value):
            self.write('AMPR{:.2f}'.format(value))

        @Feat(values={True: '1', False: '0'})
        def lf_toggle(self):
            """
            low frequency output state
            """
            return self.query('ENBL?')

        @lf_toggle.setter
        def lf_toggle(self, value):
            self.write('ENBL{:s}'.format(value))

        @Feat(values={True: '1', False: '0'})
        def rf_toggle(self):
            """
            RF output state
            """
            return self.query('ENBR?')

        @rf_toggle.setter
        def rf_toggle(self, value):
            self.write('ENBR{:s}'.format(value))

        @Feat(units='Hz')
        def frequency(self):
            """
            signal frequency
            """
            return self.query('FREQ?')

        @frequency.setter
        def frequency(self, value):
            self.write('FREQ{:.2f}'.format(value))

        @Feat()
        def rf_pll_loop_filter_mode(self):
            raise NotImplementedError

        @rf_pll_loop_filter_mode.setter
        def rf_pll_loop_filter_mode(self, value):
            raise NotImplementedError

        @Feat()
        def lf_offset(self):
            """
            low frequency offset voltage
            """
            return self.query('OFSL?')

        @lf_offset.setter
        def lf_offset(self, value):
            self.write('OFSL{:.2f}'.format(value))

        @Feat(units='degrees')
        def phase(self):
            """
            carrier phase
            """
            return self.query('PHAS?')

        @phase.setter
        def phase(self, value):
            self.write('PHAS{:.2f}'.format(value))

        @Action()
        def rel_phase(self):
            """
            sets carrier phase to 0 degrees
            """
            self.write('RPHS')
