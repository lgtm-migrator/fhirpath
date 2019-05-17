#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `fhirpath` package."""
import operator
from datetime import datetime

import pytest

from fhirpath.fql.expressions import G_
from fhirpath.fql.expressions import T_
from fhirpath.fql.expressions import and_
from fhirpath.fql.interfaces import IGroupTerm
from fhirpath.fql.interfaces import ITerm
from fhirpath.fql.types import Term
from fhirpath.fql.types import TermValue
from fhirpath.utils import PATH_INFO_CACHE
from fhirpath.utils import import_string
from fhirpath.utils import lookup_fhir_class_path


def test_term_normal(engine):
    """Sample pytest test function with the pytest fixture as an argument."""
    term = Term("Patient.active", "false")
    term.finalize(engine)

    assert term.value() is False
    assert term.arithmetic_operator == operator.and_

    term = Term("Patient.address.line", "Lane 1")
    term.finalize(engine)

    assert term.path_context.multiple is True
    assert isinstance(term.value(), str)

    # test parent path (Patient.address) context also created.
    pathname = "Patient.address"
    try:
        context = PATH_INFO_CACHE[engine.fhir_release.value][pathname]
    except KeyError:
        pytest.fail("Code should not come here! as cache should be already created")

    address_model = import_string(lookup_fhir_class_path("Address"))

    assert context.multiple is True
    assert context.type_class == address_model
    assert context.prop_name == "address"
    assert context.optional is True


def test_term_complex_operator(engine):
    """ """
    term = Term("Patient.meta.lastUpdated")
    value = TermValue(datetime.now().isoformat())
    term = term >= value
    term.finalize(engine)

    assert term.comparison_operator == operator.ge
    assert isinstance(term.value(), datetime)


def test_expression_add(engine):
    """ """
    term = and_("Patient.name.given", "Krog")
    term.finalize(engine)
    assert ITerm.providedBy(term)
    assert term.arithmetic_operator == operator.and_
    assert term.path_context.multiple is True

    term = T_("Patient.name.period.start")
    term = and_(-term, datetime.now().isoformat())

    assert term.unary_operator == operator.neg

    group = G_(term <= datetime.now().isoformat())
    group = and_(group)

