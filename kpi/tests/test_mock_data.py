# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from collections import OrderedDict

from django.contrib.auth.models import User
from django.test import TestCase

from kpi.models import Asset

F1 = {u'survey': [{u'name': u'Select_one', u'select_from': u'choice_list_1', u'required': u'true', u'label': [u'Select one', u'Seleccione uno', u'\u0627\u062e\u062a\u0631 \u0648\u0627\u062d\u062f\u0627'], u'$kuid': u'WXOeQ4Nc0', u'type': u'select_one'}, {u'name': u'Select_Many', u'select_from': u'choice_list_2', u'required': u'true', u'label': [u'Select Many', u'Muchos seleccione', u'\u0627\u062e\u062a\u0631 \u0627\u0644\u0639\u062f\u064a\u062f'], u'$kuid': u'BC6BNP91R', u'type': u'select_multiple'}, {u'$kuid': u'0e7sTrQzo', u'required': u'true', u'type': u'text', u'name': u'Text', u'label': [u'Text', u'Texto', u'\u0646\u0635']}, {u'$kuid': u'ZzKb8DeQu', u'required': u'true', u'type': u'integer', u'name': u'Number', u'label': [u'Number', u'N\xfamero', u'\u0639\u062f\u062f']}, {u'$kuid': u'gLEDxsNZo', u'required': u'true', u'type': u'decimal', u'name': u'Decimal', u'label': [u'Decimal', u'Decimal', u'\u0639\u062f\u062f \u0639\u0634\u0631\u064a']}, {u'$kuid': u'pt2w8z3Xk', u'required': u'true', u'type': u'date', u'name': u'Date', u'label': [u'Date', u'Fecha', u'\u062a\u0627\u0631\u064a\u062e']}, {u'$kuid': u'3xn0tP9AI', u'required': u'true', u'type': u'time', u'name': u'Time', u'label': [u'Time', u'Hora', u'\u0645\u0631\u0629']}, {u'$kuid': u'w0nYPBtT0', u'required': u'true', u'type': u'datetime', u'name': u'Date_and_time', u'label': [u'Date and time', u'Fecha y hora', u'\u0627\u0644\u062a\u0627\u0631\u064a\u062e \u0648 \u0627\u0644\u0648\u0642\u062a']}, {u'$kuid': u'0dovjhXG6', u'required': u'false', u'type': u'geopoint', u'name': u'GPS', u'label': [u'GPS', u'GPS', u'\u0646\u0638\u0627\u0645 \u062a\u062d\u062f\u064a\u062f \u0627\u0644\u0645\u0648\u0627\u0642\u0639']}, {u'$kuid': u'NI2fsrYZI', u'required': u'true', u'type': u'image', u'name': u'Photo', u'label': [u'Photo', u'Foto', u'\u0635\u0648\u0631\u0629 \u0641\u0648\u062a\u0648\u063a\u0631\u0627\u0641\u064a\u0629']}, {u'$kuid': u'FlfOVztW3', u'required': u'true', u'type': u'audio', u'name': u'Audio', u'label': [u'Audio', u'Audio', u'\u0633\u0645\u0639\u064a']}, {u'$kuid': u'GdNV76Ily', u'required': u'true', u'type': u'video', u'name': u'Video', u'label': [u'Video', u'V\xeddeo', u'\u0641\u064a\u062f\u064a\u0648']}, {u'$kuid': u'EDuWkTREB', u'required': u'false', u'type': u'note', u'name': u'Note_Should_not_be_displayed', u'label': [u'Note (Should not be displayed!)', u'Nota (no se represente!)', u'\u0645\u0644\u0627\u062d\u0638\u0629 (\u064a\u062c\u0628 \u0623\u0646 \u0644\u0627 \u064a\u062a\u0645 \u0639\u0631\u0636!)']}, {u'$kuid': u'hwik7tNXF', u'required': u'true', u'type': u'barcode', u'name': u'Barcode', u'label': [u'Barcode', u'C\xf3digo de barras', u'\u0627\u0644\u0628\u0627\u0631\u0643\u0648\u062f']}, {u'$kuid': u'NTBElbRcj', u'required': u'true', u'type': u'acknowledge', u'name': u'Acknowledge', u'label': [u'Acknowledge', u'Reconocer', u'\u0627\u0639\u062a\u0631\u0641']}, {u'calculation': u'1', u'$kuid': u'x6zr1MtmP', u'required': u'false', u'type': u'calculate', u'name': u'calculation'}, {u'$kuid': u'Uf89NP4VX', u'type': u'start', u'name': u'start'}, {u'$kuid': u'ZtZBY7XHX', u'type': u'end', u'name': u'end'}], u'translations': [None, u'Espa\xf1ol', u'Arabic'], u'choices': [{u'$kuid': u'xm4h0m4kK', u'list_name': u'choice_list_1', u'name': u'option_1', u'label': [u'First option', u'Primera opci\xf3n', u'\u0627\u0644\u062e\u064a\u0627\u0631 \u0627\u0644\u0623\u0648\u0644']}, {u'$kuid': u'slcf0IezR', u'list_name': u'choice_list_1', u'name': u'option_2', u'label': [u'Second option', u'Segunda opci\xf3n', u'\u0627\u0644\u062e\u064a\u0627\u0631 \u0627\u0644\u062b\u0627\u0646\u064a']}, {u'$kuid': u'G7myzY2qX', u'list_name': u'choice_list_2', u'name': u'option_1', u'label': [u'First option', u'Primera opci\xf3n', u'\u0627\u0644\u062e\u064a\u0627\u0631 \u0627\u0644\u0623\u0648\u0644']}, {u'$kuid': u'xUd28PPBs', u'list_name': u'choice_list_2', u'name': u'option_2', u'label': [u'Second option', u'Segunda opci\xf3n', u'\u0627\u0644\u062e\u064a\u0627\u0631 \u0627\u0644\u062b\u0627\u0646\u064a']}]}


class MockDataReports(TestCase):
    fixtures = ['test_data']

    def setUp(self):
        self.user = User.objects.all()[0]

        self.asset = Asset.objects.create(content=F1, owner=self.user)

        num_submissions = 4
        submission_data = OrderedDict([
            ("Select_one",
             ["option_1", "option_1", "option_2", "option_1"]),
            ("Select_Many",
             ["option_1", "option_2", "option_1 option_2", ""]),
            ("Text",
             ["a", "b", "c", "a"]),
            ("Number",
             [1, 2, 3, 2]),
            ("Decimal",
             [1.5, 2.5, 3.5, 3.5]),
            ("Date",
             ["2016-06-0%d" % n for n in [1, 2, 3, 5]]),
            ("Time",
             ["%d:00:00" % n for n in [1, 2, 3, 5]]),
            ("Date_and_time",
             ["2016-06-0%dT12:00:00.000-04:00" % n for n in [1, 2, 3, 5]]),
            ("GPS",
             ["1%d.43 -2%d.54 1 0" % (n, n) for n in [5, 7, 8, 5]]),
            ("Photo",
             ["photo_%d.jpg" % (n) for n in [1, 2, 3, 4]]),
            ("Audio",
             ["audio_%d.jpg" % (n) for n in [4, 3, 2, 1]]),
            ("Video",
             ["video_%d.jpg" % (n) for n in [6, 7, 8, 9]]),
            ("Note_Should_not_be_displayed",
             [None, None, None, None]),
            ("Barcode",
             ["barcode%d" % (n) for n in [9, 7, 7, 6]]),
            ("Acknowledge",
             [None, None, None, None]),
            ("calculation",
             ["1", "1", "1", "1"]),
            ("start",
             ["2016-06-0%dT12:00:00.000-04:00" % n for n in [1, 2, 3, 4]]),
            ("end",
             ["2016-06-0%dT11:0%d:00.000-04:00" % (n, n) for n in [1, 2, 3, 4]]),
        ])

        submissions = []
        for i in range(0, num_submissions):
            submissions.append(OrderedDict([
                (key, submission_data[key][i]) for key in submission_data.keys()
                ]))

        self.asset.deploy(backend='mock')
        self.asset.save()
        v_uid = self.asset.latest_deployed_version.uid
        for submission in submissions:
            submission.update({
                '__version__': v_uid
            })
            self.asset.deployment._mock_submission(submission)
        self.asset.save(create_version=False)

    def test_has_version(self):
        self.assertEqual(self.asset.asset_versions.count(), 2)
        self.assertTrue(self.asset.has_deployment)
        self.assertEqual(self.asset.deployment._submission_count(), 4)