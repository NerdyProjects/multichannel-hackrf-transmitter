#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: matthias
# GNU Radio version: 3.8.0.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
import SimpleXMLRPCServer
import threading
import osmosdr
import time
from gnuradio import qtgui

class polyphase(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "polyphase")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 33333
        self.quad_mul = quad_mul = 6
        self.quad_rate = quad_rate = samp_rate*quad_mul
        self.num_banks = num_banks = 20
        self.taps = taps = firdes.low_pass_2(5, num_banks*quad_rate, 60e3, 60e3, 80, firdes.WIN_BLACKMAN_HARRIS)
        self.variable_qtgui_entry_0 = variable_qtgui_entry_0 = len(taps)
        self.preemphasis_high_corner = preemphasis_high_corner = 13e3

        ##################################################
        # Blocks
        ##################################################
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer(('localhost', 8080), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self._variable_qtgui_entry_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_entry_0_tool_bar.addWidget(Qt.QLabel('filter length' + ": "))
        self._variable_qtgui_entry_0_line_edit = Qt.QLineEdit(str(self.variable_qtgui_entry_0))
        self._variable_qtgui_entry_0_tool_bar.addWidget(self._variable_qtgui_entry_0_line_edit)
        self._variable_qtgui_entry_0_line_edit.returnPressed.connect(
            lambda: self.set_variable_qtgui_entry_0(int(str(self._variable_qtgui_entry_0_line_edit.text()))))
        self.top_grid_layout.addWidget(self._variable_qtgui_entry_0_tool_bar)
        self.rational_resampler_xxx_0_0_0_0_0 = filter.rational_resampler_fff(
                interpolation=quad_mul,
                decimation=1,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0_0_0_0 = filter.rational_resampler_fff(
                interpolation=quad_mul,
                decimation=1,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_fff(
                interpolation=quad_mul,
                decimation=1,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=quad_mul,
                decimation=1,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=quad_mul,
                decimation=1,
                taps=None,
                fractional_bw=None)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            quad_rate*num_banks, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)
        self.pfb_synthesizer_ccf_0 = filter.pfb_synthesizer_ccf(
            num_banks,
            taps,
            False)
        self.pfb_synthesizer_ccf_0.set_channel_map([1, 2, 6, 7, 8])
        self.pfb_synthesizer_ccf_0.declare_sample_delay(0)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_sink_0.set_sample_rate(quad_rate*num_banks)
        self.osmosdr_sink_0.set_center_freq(93200000, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(0, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.blocks_short_to_float_0_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_ff(0)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(30e-6)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(30e-6)
        self.blocks_file_source_0_0_0 = blocks.file_source(gr.sizeof_short*1, '../../samples/3.aud', True, 0, 0)
        self.blocks_file_source_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_short*1, '../../samples/2.aud', True, 0, 0)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_short*1, '../../samples/1.aud', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.analog_frequency_modulator_fc_0_0_0_0_0 = analog.frequency_modulator_fc(0.8)
        self.analog_frequency_modulator_fc_0_0_0_0 = analog.frequency_modulator_fc(0.8)
        self.analog_frequency_modulator_fc_0_0_0 = analog.frequency_modulator_fc(0.8)
        self.analog_frequency_modulator_fc_0_0 = analog.frequency_modulator_fc(0.8)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(0.8)
        self.analog_fm_preemph_0_0_0_0_0 = analog.fm_preemph(fs=quad_rate, tau=50e-6, fh=preemphasis_high_corner)
        self.analog_fm_preemph_0_0_0_0 = analog.fm_preemph(fs=quad_rate, tau=50e-6, fh=preemphasis_high_corner)
        self.analog_fm_preemph_0_0_0 = analog.fm_preemph(fs=quad_rate, tau=50e-6, fh=preemphasis_high_corner)
        self.analog_fm_preemph_0_0 = analog.fm_preemph(fs=quad_rate, tau=50e-6, fh=preemphasis_high_corner)
        self.analog_fm_preemph_0 = analog.fm_preemph(fs=quad_rate, tau=50e-6, fh=preemphasis_high_corner)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.rational_resampler_xxx_0_0_0_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.rational_resampler_xxx_0_0_0_0_0, 0))
        self.connect((self.analog_fm_preemph_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.analog_fm_preemph_0_0, 0), (self.analog_frequency_modulator_fc_0_0, 0))
        self.connect((self.analog_fm_preemph_0_0_0, 0), (self.analog_frequency_modulator_fc_0_0_0, 0))
        self.connect((self.analog_fm_preemph_0_0_0_0, 0), (self.analog_frequency_modulator_fc_0_0_0_0, 0))
        self.connect((self.analog_fm_preemph_0_0_0_0_0, 0), (self.analog_frequency_modulator_fc_0_0_0_0_0, 0))
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.pfb_synthesizer_ccf_0, 0))
        self.connect((self.analog_frequency_modulator_fc_0_0, 0), (self.pfb_synthesizer_ccf_0, 1))
        self.connect((self.analog_frequency_modulator_fc_0_0_0, 0), (self.pfb_synthesizer_ccf_0, 2))
        self.connect((self.analog_frequency_modulator_fc_0_0_0_0, 0), (self.pfb_synthesizer_ccf_0, 3))
        self.connect((self.analog_frequency_modulator_fc_0_0_0_0_0, 0), (self.pfb_synthesizer_ccf_0, 4))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_short_to_float_0_0, 0))
        self.connect((self.blocks_file_source_0_0_0, 0), (self.blocks_short_to_float_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_short_to_float_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_short_to_float_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.pfb_synthesizer_ccf_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.pfb_synthesizer_ccf_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_fm_preemph_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_fm_preemph_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.analog_fm_preemph_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0, 0), (self.analog_fm_preemph_0_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0_0, 0), (self.analog_fm_preemph_0_0_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "polyphase")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_quad_rate(self.samp_rate*self.quad_mul)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_quad_mul(self):
        return self.quad_mul

    def set_quad_mul(self, quad_mul):
        self.quad_mul = quad_mul
        self.set_quad_rate(self.samp_rate*self.quad_mul)

    def get_quad_rate(self):
        return self.quad_rate

    def set_quad_rate(self, quad_rate):
        self.quad_rate = quad_rate
        self.set_taps(firdes.low_pass_2(5, self.num_banks*self.quad_rate, 60e3, 60e3, 80, firdes.WIN_BLACKMAN_HARRIS))
        self.blocks_throttle_1.set_sample_rate(self.quad_rate*self.num_banks)
        self.osmosdr_sink_0.set_sample_rate(self.quad_rate*self.num_banks)
        self.qtgui_sink_x_0.set_frequency_range(0, self.quad_rate*self.num_banks)

    def get_num_banks(self):
        return self.num_banks

    def set_num_banks(self, num_banks):
        self.num_banks = num_banks
        self.set_taps(firdes.low_pass_2(5, self.num_banks*self.quad_rate, 60e3, 60e3, 80, firdes.WIN_BLACKMAN_HARRIS))
        self.blocks_throttle_1.set_sample_rate(self.quad_rate*self.num_banks)
        self.osmosdr_sink_0.set_sample_rate(self.quad_rate*self.num_banks)
        self.qtgui_sink_x_0.set_frequency_range(0, self.quad_rate*self.num_banks)

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.set_variable_qtgui_entry_0(len(self.taps))
        self.pfb_synthesizer_ccf_0.set_taps(self.taps)

    def get_variable_qtgui_entry_0(self):
        return self.variable_qtgui_entry_0

    def set_variable_qtgui_entry_0(self, variable_qtgui_entry_0):
        self.variable_qtgui_entry_0 = variable_qtgui_entry_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_entry_0_line_edit, "setText", Qt.Q_ARG("QString", str(self.variable_qtgui_entry_0)))

    def get_preemphasis_high_corner(self):
        return self.preemphasis_high_corner

    def set_preemphasis_high_corner(self, preemphasis_high_corner):
        self.preemphasis_high_corner = preemphasis_high_corner



def main(top_block_cls=polyphase, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
