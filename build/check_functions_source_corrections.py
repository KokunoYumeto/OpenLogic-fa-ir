"""Static exact-source QA for the combined OLFUN/OLSIZ/OLEMPH/OLVIS Farsi overlay.

The filename is retained for compatibility with the original functions-only
gate. This checker never runs TeX. Native environment capture, trace emission,
extraction, and page layout remain separate guarded-build gates.
"""
from __future__ import annotations

from pathlib import Path
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import re


ROOT = Path(__file__).resolve().parents[1]
FA = ROOT / "source/locale/fa-IR"
OVERLAY = FA / "standalone/source-corrections.tex"
ERRATA = FA / "standalone-errata.tex"
BODY = FA / "standalone/body.tex"
RUNTIME = FA / "standalone/runtime.tex"
TYPOGRAPHY = FA / "standalone/typography.tex"
DRIVER = FA / "open-logic-standalone-fa-IR.tex"
GENERATED_LEDGER = FA / "standalone/generated-ledger.tex"
DERIVED_ROOT = FA / "standalone/generated-source-corrections"
DERIVED_CONTENT = DERIVED_ROOT / "content"
DERIVED_MANIFEST = DERIVED_ROOT / "MANIFEST.json"
DERIVED_GENERATOR = ROOT / "build/generate_source_correction_overlays.py"
UTF8_BOM = b"\xef\xbb\xbf"
FIXTURE = ROOT / "evidence/SOURCE_CORRECTIONS_PROBE_FIXTURE.json"
SOURCE_ROOT = FA / "content/sets-functions-relations"
CONTENT_ROOT = FA / "content"

STAGING = Path(
    "C:/interlanguage-task-state/openlogic-internationalization/persian-openlogic/"
    "standalone-staging/STAGED_FILE_MANIFEST.json"
)
STAGING_SHA256 = "97864216624a65e137332d70f6563515c3a17b304362e4267d2d589d4ded4103"

FUNCTIONS_AUDIT = Path(
    "C:/interlanguage-task-state/openlogic-internationalization/source-audits/"
    "2026-09-04-functions"
)
SIZE_AUDIT = Path(
    "C:/interlanguage-task-state/openlogic-internationalization/source-audits/"
    "2026-09-04-size-of-sets"
)
AUDIT_REVIEW_FUNCTIONS = FUNCTIONS_AUDIT / "REVIEW.md"
AUDIT_FINDINGS_FUNCTIONS = FUNCTIONS_AUDIT / "FINDINGS.json"
AUDIT_REVIEW_SIZE = SIZE_AUDIT / "REVIEW.md"
AUDIT_FINDINGS_SIZE = SIZE_AUDIT / "FINDINGS.json"
AUDIT_RETRACTION = SIZE_AUDIT / "RETRACTION_OLSIZ_011.json"
AUDIT_TOMBSTONE = SIZE_AUDIT / "SUPPLEMENT-OLSIZ-011.json"
AUDIT_HASHES = {
    AUDIT_REVIEW_FUNCTIONS: "bc183d34b6ac57cc00e2df76d00277cdd2fabee293d12beb142d2e27344f8d24",
    AUDIT_FINDINGS_FUNCTIONS: "eee57facbea44f65a19a816fb12cbc86be0b18e21dcffeeed943f52f7e332960",
    AUDIT_REVIEW_SIZE: "26913176baacbda5ae8a47bcc82ccf0366b0763313e6eeeb45df59e64249a1f9",
    AUDIT_FINDINGS_SIZE: "9b6e836c8432eb75d331913983603796d6557da6ec3ad71b846b2a248374cd07",
    AUDIT_RETRACTION: "b495d66165f3c7f0b32d61b0b106c402badcc6e4e6a130442734c8f883dd5adc",
    AUDIT_TOMBSTONE: "b1b9f8ad296bc8d718a17514cdb91c61a8c1ea537a1231604f862551406b35bf",
}

AUDIT_IDS = ["OLFUN-20260904", "OLSIZ-20260904"]
DOCUMENT_TEXT_REPAIR_FAMILIES = ["OLEMPH-20260905", "OLVIS-20260905"]
FUNCTION_FINDINGS = [
    "OLFUN-001", "OLFUN-002", "OLFUN-003", "OLFUN-004", "OLFUN-005",
]
SIZE_FINDINGS = [
    "OLSIZ-001", "OLSIZ-002", "OLSIZ-003", "OLSIZ-004", "OLSIZ-005",
    "OLSIZ-006", "OLSIZ-007", "OLSIZ-008", "OLSIZ-009", "OLSIZ-010",
]
SEMANTIC_FINDINGS = FUNCTION_FINDINGS + SIZE_FINDINGS
EMPH_FINDINGS = [f"OLEMPH-{index:03d}" for index in range(1, 8)]
LAYOUT_FINDINGS = [
    "OLVIS-0362", "OLVIS-0379", "OLVIS-0391",
    "OLVIS-0569", "OLVIS-0570", "OLVIS-0599",
    "OLVIS-0091", "OLVIS-0133-OVERFLOW", "OLVIS-0133-COMMA",
    "OLVIS-0164", "OLVIS-0165", "OLVIS-0193", "OLVIS-0220",
    "OLVIS-0273", "OLVIS-0286", "OLVIS-0526", "OLVIS-0527",
]
RESIDUAL_OVERFLOW_FINDINGS = [
    "OLVIS-0091", "OLVIS-0133-OVERFLOW", "OLVIS-0164", "OLVIS-0165",
    "OLVIS-0193", "OLVIS-0220", "OLVIS-0273", "OLVIS-0286",
    "OLVIS-0526", "OLVIS-0527",
]
RESIDUAL_ADDITIONAL_FINDINGS = RESIDUAL_OVERFLOW_FINDINGS + ["OLVIS-0133-COMMA"]
LINEBREAK_REPLACES_TIE_FINDINGS = {
    "OLVIS-0362", "OLVIS-0391", "OLVIS-0569",
}
DOCUMENT_TEXT_FINDINGS = EMPH_FINDINGS + LAYOUT_FINDINGS
CURRENT_FINDINGS = SEMANTIC_FINDINGS + DOCUMENT_TEXT_FINDINGS
PRIOR_EXACT_RULE_COUNT = 28
PRIOR_RUNTIME_EVENT_COUNT = 28

# Declaration order is part of the contract. OLSIZ-002 executes last because
# it is captured by answers.sty and corrected only during deferred readback.
EXPECTED_DECLARATIONS = [
    ("OLP-0021", "ex", "OLFUN-002", "functions/function-basics.tex"),
    ("OLP-0021", "ex", "OLFUN-003", "functions/function-basics.tex"),
    ("OLP-0023", "explain", "OLFUN-004", "functions/functions-relations.tex"),
    ("OLP-0023", "explain", "OLFUN-005", "functions/functions-relations.tex"),
    ("OLP-0024", "prop", "OLFUN-001-THEOREM", "functions/inverses.tex"),
    ("OLP-0024", "proof", "OLFUN-001-PROOF", "functions/inverses.tex"),
    ("OLP-0029", "ex", "OLSIZ-001", "size-of-sets/enumerability.tex"),
    ("OLP-0031", "prob", "OLSIZ-002", "size-of-sets/pairing.tex"),
    ("OLP-0032", "explain", "OLSIZ-003", "size-of-sets/pairing-alt.tex"),
    ("OLP-0034", "proof", "OLSIZ-004", "size-of-sets/reduction.tex"),
    ("OLP-0034", "explain", "OLSIZ-005", "size-of-sets/reduction.tex"),
    ("OLP-0035", "proof", "OLSIZ-006", "size-of-sets/equinumerous-sets.tex"),
    ("OLP-0036", "proof", "OLSIZ-007", "size-of-sets/comparing-size.tex"),
    ("OLP-0039", "proof", "OLSIZ-008+009", "size-of-sets/non-enumerability-alt.tex"),
    ("OLP-0040", "proof", "OLSIZ-010", "size-of-sets/reduction-alt.tex"),
]
SOURCE_EXPECTED_DECLARATIONS = EXPECTED_DECLARATIONS
EXPECTED = {
    rule: (unit, environment, relative)
    for unit, environment, rule, relative in SOURCE_EXPECTED_DECLARATIONS
}
HISTORICAL_EXPECTED_TRACE_DECLARATIONS = [
    *EXPECTED_DECLARATIONS[:7],
    *EXPECTED_DECLARATIONS[8:],
    EXPECTED_DECLARATIONS[7],
]
HISTORICAL_EXPECTED_EVENTS = [
    (unit, environment, rule, "1")
    for unit, environment, rule, _relative in HISTORICAL_EXPECTED_TRACE_DECLARATIONS
]
EMPH_EXPECTED_DECLARATIONS = [
    ("OLP-0179", "document-text", "OLEMPH-001", "first-order-logic/beyond/intuitionistic-logic.tex"),
    ("OLP-0179", "document-text", "OLEMPH-002", "first-order-logic/beyond/intuitionistic-logic.tex"),
    ("OLP-0179", "document-text", "OLEMPH-003", "first-order-logic/beyond/intuitionistic-logic.tex"),
    ("OLP-0180", "document-text", "OLEMPH-004", "first-order-logic/beyond/modal-logics.tex"),
    ("OLP-0180", "document-text", "OLEMPH-005", "first-order-logic/beyond/modal-logics.tex"),
    ("OLP-0180", "document-text", "OLEMPH-006", "first-order-logic/beyond/modal-logics.tex"),
    ("OLP-0180", "document-text", "OLEMPH-007", "first-order-logic/beyond/modal-logics.tex"),
]
EMPH_EXPECTED = {
    rule: (unit, environment, relative)
    for unit, environment, rule, relative in EMPH_EXPECTED_DECLARATIONS
}
LAYOUT_EXPECTED_DECLARATIONS = [
    ("OLP-0362", "document-text", "OLVIS-0362", "lambda-calculus/syntax/alpha.tex"),
    ("OLP-0379", "document-text", "OLVIS-0379", "lambda-calculus/lambda-definability/fixpoints.tex"),
    ("OLP-0391", "document-text", "OLVIS-0391", "many-valued-logic/syntax-and-semantics/sublogics.tex"),
    ("OLP-0569", "document-text", "OLVIS-0569", "set-theory/replacement/limofsize.tex"),
    ("OLP-0570", "document-text", "OLVIS-0570", "set-theory/replacement/absinf.tex"),
    ("OLP-0599", "document-text", "OLVIS-0599", "set-theory/choice/banach.tex"),
    ("OLP-0091", "document-text", "OLVIS-0091", "first-order-logic/natural-deduction/proof-theoretic-notions.tex"),
    ("OLP-0133", "document-text", "OLVIS-0133-OVERFLOW", "first-order-logic/completeness/identity.tex"),
    ("OLP-0133", "document-text", "OLVIS-0133-COMMA", "first-order-logic/completeness/identity.tex"),
    ("OLP-0164", "document-text", "OLVIS-0164", "first-order-logic/syntax-and-semantics/assignments.tex"),
    ("OLP-0165", "document-text", "OLVIS-0165", "first-order-logic/syntax-and-semantics/extensionality.tex"),
    ("OLP-0193", "document-text", "OLVIS-0193", "model-theory/models-of-arithmetic/standard-models.tex"),
    ("OLP-0220", "document-text", "OLVIS-0220", "computability/recursive-functions/sequences.tex"),
    ("OLP-0273", "document-text", "OLVIS-0273", "turing-machines/undecidability/trakhtenbrot.tex"),
    ("OLP-0286", "document-text", "OLVIS-0286", "incompleteness/arithmetization-syntax/proofs-in-lk.tex"),
    ("OLP-0526", "document-text", "OLVIS-0526", "counterfactuals/minimal-change-semantics/antecedent-strengthening.tex"),
    ("OLP-0527", "document-text", "OLVIS-0527", "counterfactuals/minimal-change-semantics/transitivity.tex"),
]
DOCUMENT_TEXT_EXPECTED_DECLARATIONS = (
    EMPH_EXPECTED_DECLARATIONS + LAYOUT_EXPECTED_DECLARATIONS
)
DOCUMENT_TEXT_EXPECTED = {
    rule: (unit, environment, relative)
    for unit, environment, rule, relative in DOCUMENT_TEXT_EXPECTED_DECLARATIONS
}
CURRENT_EXPECTED_DECLARATIONS = (
    SOURCE_EXPECTED_DECLARATIONS + DOCUMENT_TEXT_EXPECTED_DECLARATIONS
)
# Runtime order follows the generated standalone ledger, not declaration order.
# The historical environment corrections execute first, including the OLSIZ-002
# deferred problem at the end of the size-of-sets run.  OLP-0091 is then seen in
# PL and FOL around the intervening FOL units.  OLVIS-0273 is materialized in
# its derived physical input before answers.sty performs deferred serialization.
CURRENT_EXPECTED_EVENTS = [
    *[(unit, environment, rule, "1")
      for unit, environment, rule, _relative in EXPECTED_DECLARATIONS[:7]],
    *[(unit, environment, rule, "1")
      for unit, environment, rule, _relative in EXPECTED_DECLARATIONS[8:]],
    ("OLP-0031", "prob", "OLSIZ-002", "1"),
    ("OLP-0091", "document-text", "OLVIS-0091", "1"),
    ("OLP-0164", "document-text", "OLVIS-0164", "1"),
    ("OLP-0165", "document-text", "OLVIS-0165", "1"),
    ("OLP-0091", "document-text", "OLVIS-0091", "2"),
    ("OLP-0133", "document-text", "OLVIS-0133-OVERFLOW", "1"),
    ("OLP-0133", "document-text", "OLVIS-0133-COMMA", "1"),
    *[(unit, environment, rule, "1")
      for unit, environment, rule, _relative in EMPH_EXPECTED_DECLARATIONS],
    ("OLP-0193", "document-text", "OLVIS-0193", "1"),
    ("OLP-0220", "document-text", "OLVIS-0220", "1"),
    ("OLP-0273", "document-text", "OLVIS-0273", "1"),
    ("OLP-0286", "document-text", "OLVIS-0286", "1"),
    ("OLP-0362", "document-text", "OLVIS-0362", "1"),
    ("OLP-0379", "document-text", "OLVIS-0379", "1"),
    ("OLP-0391", "document-text", "OLVIS-0391", "1"),
    ("OLP-0526", "document-text", "OLVIS-0526", "1"),
    ("OLP-0527", "document-text", "OLVIS-0527", "1"),
    ("OLP-0569", "document-text", "OLVIS-0569", "1"),
    ("OLP-0570", "document-text", "OLVIS-0570", "1"),
    ("OLP-0599", "document-text", "OLVIS-0599", "1"),
]
PRIOR_28_EXPECTED_EVENTS = [
    *[(unit, environment, rule, "1")
      for unit, environment, rule, _relative in EXPECTED_DECLARATIONS[:7]],
    *[(unit, environment, rule, "1")
      for unit, environment, rule, _relative in EXPECTED_DECLARATIONS[8:]],
    *[(unit, environment, rule, "1")
      for unit, environment, rule, _relative in EMPH_EXPECTED_DECLARATIONS],
    *[(unit, environment, rule, "1")
      for unit, environment, rule, _relative in LAYOUT_EXPECTED_DECLARATIONS[:6]],
    ("OLP-0031", "prob", "OLSIZ-002", "1"),
]
SPECIAL_RULE_TO_FINDINGS = {
    "OLFUN-001-THEOREM": ["OLFUN-001"],
    "OLFUN-001-PROOF": ["OLFUN-001"],
    "OLSIZ-008+009": ["OLSIZ-008", "OLSIZ-009"],
}
EXPECTED_SEMANTIC_MAPPING_COUNTS = Counter({
    **{finding: 1 for finding in SEMANTIC_FINDINGS},
    "OLFUN-001": 2,
})
EXPECTED_BODY_HASHES = {
    "OLFUN-002": ("4789945cd11d0b189334d2ab6b85dba25263a2db5e893f1a2cf1d2588b6e51f9", "09554397df91f1a1606a1456cfcfaa80d61ad3f8b0e2faf9dacdd654f460cd44"),
    "OLFUN-003": ("0bc8d84a42fa189633215fbf9dfd4626d1889ea200ede7e9f2be00b774e0f025", "585e65436c218df4158eb8e145cb173292e39820b2a2180867e7c2c29e355243"),
    "OLFUN-004": ("72a6c20738ceda87b4cd495263aad867ca59ba96f0343e87c0cda93bf4013578", "e4d95c0e6b8afe11eb242a0d06f23172e3bb0b50d3cb08bf31b245b7115ff340"),
    "OLFUN-005": ("a454212a00b8e37b8c2d03b2aaba383b835da6f686d12ef3175443c51cc67a36", "a5be256b344bd9ba5d63a49fcd1f256bfe9db749bb88bd9a7d19a321c52e8ec2"),
    "OLFUN-001-THEOREM": ("8aebf99ed390beac4da4a44b0aa7399c77d2bf12e96932f779b63a4c5fbd1ae2", "e294da065edf0091fc5694486cf8c51c6f0438d3b2e778938739b073250b054e"),
    "OLFUN-001-PROOF": ("bfe7fc23f53f01373b86c6204e24c8a2335c49187e23fb9b5c92a2b5cf41424b", "7474ceccbc27f207420b9e7739af6417a777c6be88de8096868f4ef0418ae7fe"),
    "OLSIZ-001": ("868af0e666caa26a370e49744ae99f7970a5a3404cb3c1f27282e5b6c7a3232a", "f82513c20eb665bc8ce088f31d9e1799470e94e4b608a7d15b59959a4ca062ea"),
    "OLSIZ-002": ("0c3dcb99216e95d84b3ae01e396ae820f7626e48183f727f9b2fc0813133fb8c", "ddc7ffb72d647e5467f2bddbe0840d3ffc378496bedf4fe94efdd5916e843154"),
    "OLSIZ-003": ("9c0c8d9b8d2603fcbf40b98cea77332166ecec36be2cfbf4af61abbd35a2fbe1", "b99bfce84e543a285f8f5b1a48bcaf3d1a1a92a4d92eb4f8ab2ed644f4adc4a7"),
    "OLSIZ-004": ("0ede765e0176e77e4ee0eadf2902e3049115c1daeb4fbda730a74fc964158c48", "c12fe008cdb4dbff13112dc02bb62b48ed6c6d4ceda98860c033d50364a976e6"),
    "OLSIZ-005": ("b7d36db74bc7d2a5ed19b47ee2ed4bc7231d99e69aace9b78cdaeb5faa45d186", "e8bab2b2cc3eeb45a792d4fb584eaabbedfbb8a5124176cc03574fdd281c5aff"),
    "OLSIZ-006": ("6d6aece0a1e6b8d467a83809c6b9a4a8292e1490b9e737828fafbbb698998f59", "1c381c9c1678b75fe998db40277de02ba4874023fcc0b1c49577be047b2c81d3"),
    "OLSIZ-007": ("c8b11ddde014e04444d02fb0b91f2cff98eeb033f94408465617bf325ebfc098", "1fb5df863da40aae31d402eade7e8616cbade25a3868d6950fad770cc73c36ef"),
    "OLSIZ-008+009": ("bd99f819737871bde7f512f0d28efb0c2b9e7e4ae6ace69e1b9f2d88015738d6", "2eafb7f049c46e89ab7b7436286e67c18e0a8752888ebaac40e3bde4e0ad4147"),
    "OLSIZ-010": ("974a417d4cc98db4081e22254f41965de782904f5684dec7d4d18486d2f5e472", "8271d7506695ac5ef266107991fdd2fd6e5c33ca91397593b424952c25327634"),
}
EMPH_EXPECTED_BODY_HASHES = {
    "OLEMPH-001": ("f67b9af844d97eca0adca36758ea6efff1f103bae4dce33ebe554c57d81d8d25", "cd0f13c2396876f41a56e8868d3b6defccf60ae01103477adffa4f31a57fc0f2"),
    "OLEMPH-002": ("aef2e302e869eb60c1dfd52015a56cd549fac4be2b68b64c69343ae53d265841", "d6a1eea9183026cc4fb2e9991df2917d13e044e3dcfa448f5f26eaac3c61e901"),
    "OLEMPH-003": ("29bc9f6623d3668ab6471b7c65f45f2a5d821b948a8e608cdf9f7dcbef2942da", "948cf6c2a666916df9e1f18e6ed112450cf1b82ea3651aa41476e5addf0e69ad"),
    "OLEMPH-004": ("76d734c2a490718b2b425a6b9143ed233c859fce114a4c9c730ce4d2d687c4a9", "3ab96f5b1db9180735def5503e6b68b1ae7845eb57a0f11ecc7d2e2daa73d2f6"),
    "OLEMPH-005": ("83265dd87d954be19fbb3d1d58c74db26adbaec6fb70518c71a2ab82323752ea", "b09b24fce1f7da1f077dc880e14048c510e25d9cdc5fe186716254d9486331e2"),
    "OLEMPH-006": ("01acb6caddc64db9d2d7f75f76e740765e897d207e2e531034c3d1434cdc2977", "672c5844bc3e6ea65b58c4b07a4b00ecd34fdb612a1c4515d890bef8a50770d1"),
    "OLEMPH-007": ("dd99846b689cf8c5af2759be0edbb0c0580871e2d779cc561e73cd8e97bd81f9", "1f173df44d339d47d6375294d4aed57ca795d01dab34d38bee07e147951b60e3"),
}
LAYOUT_EXPECTED_BODY_HASHES = {
    "OLVIS-0362": ("19f24e676c6eeac4f45bc104f4184fda1bc5cad593740f83e5e7c40ef4565745", "53161fafc5e7dfc40dd01afaa8daf5ba3507c190007e8b206d2e20bce6ed1531"),
    "OLVIS-0379": ("2f42bffe0b4aaf2b5ef5ad7d8c33928e16803e24778adc396a5fa7cefa763ef2", "71b68b45f78fbc18c83267ee2228dd44e10457faac7e25998397061b84c5c8d2"),
    "OLVIS-0391": ("a5a1f79a562c1bed64123a7490dc4ea0b3a9f7f8b708ada141175f7167472a1d", "34d721f1c50b780796fbb69f211e6ec01e58e7f91021d4c44ce6d982f7e8e47d"),
    "OLVIS-0569": ("db4d78da2fc0e1dd1f7fb2730f6ee9b298bea134537a8985a757cc6f1e9012ed", "9007b1631da301da2537b28b32b65a5c50c21c7fc762e4b9c06bd67a8ff5da1a"),
    "OLVIS-0570": ("2bf1aa7d70ad601e0af0f23ac2c6ac5de8f22e12d92549a2a0335731e16f588a", "06a52661c47161df91752826be89afba5669e304555c694fb6eb72d7d7520315"),
    "OLVIS-0599": ("a0166c7f0eda02a9b5bea4c944a68f047447da8a2ec33d02c186d376b65903d4", "846ae52c1ed7e78a18d5a5779e77bec3358d62e849e36caa9c4ef6f321d16046"),
    "OLVIS-0091": ("29bcc9e6e38220c5b75c90b53f341cdedbf62bea6b6a80d01439abb07820e498", "a4f664fdb7574555f01246865c42d08d8c16b61efb089d3c2863549f82b2464f"),
    "OLVIS-0133-OVERFLOW": ("286bce5090791507da648522d27ccf9afc34bc0125b9d045c16f83c832953624", "b60e1f971754b5c7d2635198e61b7f5ec5155ea4fd6971a55d2fa76e8976f5e7"),
    "OLVIS-0133-COMMA": ("429d89668a21629211a50c9518407c406de6adcf12b1d158f1ca2a625cd2ca0f", "1e9e8131976bcdf017d7661eac1dc25a9a802b3b0eb63d876832429ce0283971"),
    "OLVIS-0164": ("197dd8b2663a7682f9017c48aa24c9117026240f85b2306e80e74c3ebf7659ce", "006615b3a50462d13f5a5c2da97c1dcc8a067dd81fe7620357f934a1936a27b8"),
    "OLVIS-0165": ("3b1168190c9e85e906bf0d98de9a84dd05b5869189a777a5a2dad61e7d9b98f4", "bae983030f9e5116434e66acc32e9609f68542c7f89d78628f624f5f5b44b540"),
    "OLVIS-0193": ("a08f09d7c9121735b6fd23ca9bf79313f6244a5a806b61e2c3a3f4e8f1e35309", "1da5a31dc7440df7818395a0206e0cfa00010c2aa5a260d82991a5706a37fff0"),
    "OLVIS-0220": ("434bdf5053dd55424f2535b3fe94d404944975fbefdffbcd12788a43cc73201a", "c25a8ba85a976ac69de99805d0a1935036495d16940a0aba0e5f8d02d2c31757"),
    "OLVIS-0273": ("2fe07f85c39a9165272b4c0699c1188b8ee8fe560a153eac8e49d730545c7fa3", "d3f8cad77a3fe620cfbb59811e1de9bed887d9d9d9492df584dee63377912fe1"),
    "OLVIS-0286": ("29fc444a20701acd426706a7c0e5da37696bffa66fde3a8257e4befc20c9ca8d", "168fec467df8e97425245cb786145f56bf5982e12897f83b2ae2fdc109d00a23"),
    "OLVIS-0526": ("51e8518cc302efe34c791ff956f31c0db2906665053a3add5522a4ab74329753", "18be06a38b386739fd97479a04ea6d199ac4237734cf0a1fbfcfbb0e1e7c94f4"),
    "OLVIS-0527": ("1316cfc5ecdf579603c3ab6926f7439053f2364b8a5ecd4bc729143cc728056a", "fca7dc53971f1c3b13814542ef0d75c918247c5ee32ee334b659a4cd37dc12c6"),
}
DOCUMENT_TEXT_EXPECTED_BODY_HASHES = {
    **EMPH_EXPECTED_BODY_HASHES,
    **LAYOUT_EXPECTED_BODY_HASHES,
}
EMPH_SOURCE_IDENTITIES = {
    "first-order-logic/beyond/intuitionistic-logic.tex": {
        "bytes": 15694,
        "sha256": "ff0733f6aa24eebeb90981c6c6a4ccbd878fc197c2abb79649adb5b082824f91",
        "malformed_emph_occurrences": 3,
    },
    "first-order-logic/beyond/modal-logics.tex": {
        "bytes": 6250,
        "sha256": "47b263bcf4da43c9f390b7e5a8c8c285f5ebb7b91e17b4e7fdb92db62f9a8929",
        "malformed_emph_occurrences": 4,
    },
}
LAYOUT_SOURCE_IDENTITIES = {
    "lambda-calculus/syntax/alpha.tex": {
        "bytes": 12883,
        "sha256": "7dd420912e869e9aa49c71d390c687ab7270025b8b1069a6b292547aa6ec638b",
    },
    "lambda-calculus/lambda-definability/fixpoints.tex": {
        "bytes": 9093,
        "sha256": "11298b621b02ac40e7e3f3962fc57bfa690f21daf6f7e5feb9a57078991428c7",
    },
    "many-valued-logic/syntax-and-semantics/sublogics.tex": {
        "bytes": 4846,
        "sha256": "3517f9bbafcb11b51143fb2c6ad4977004cbf838c50b20e7b74aa3a30491fa92",
    },
    "set-theory/replacement/limofsize.tex": {
        "bytes": 4911,
        "sha256": "6f6adeca73424069e15ef08d01fd6c53152859c5b50df348a3196c434888cab2",
    },
    "set-theory/replacement/absinf.tex": {
        "bytes": 8716,
        "sha256": "ad0f7d5272b418c04a6be416df53aab0a10df5922c5c041bc77c3500dd63fcff",
    },
    "set-theory/choice/banach.tex": {
        "bytes": 6178,
        "sha256": "73d279e7d0ac690b685d232aa5817aa5bae2934c70f8d7dc83a6a488298dc421",
    },
    "first-order-logic/natural-deduction/proof-theoretic-notions.tex": {
        "bytes": 6435,
        "sha256": "462e7eae7f7167718d48dbeaa322f31d2d13a0372b71ea169812a9f284dca178",
    },
    "first-order-logic/completeness/identity.tex": {
        "bytes": 9773,
        "sha256": "c3731eeaf405d2703c54d6ec9d8ce460404dc07f4ea814a0e9e264f9f4bd2fee",
    },
    "first-order-logic/syntax-and-semantics/assignments.tex": {
        "bytes": 17601,
        "sha256": "b177da8800cbd10172d1174075c55a2f5ecd68b6231451ca4847f785b8f4dea7",
    },
    "first-order-logic/syntax-and-semantics/extensionality.tex": {
        "bytes": 6423,
        "sha256": "d74041167152da05317cb088d33aafb03d596909d59147bc747951ebed3a5f81",
    },
    "model-theory/models-of-arithmetic/standard-models.tex": {
        "bytes": 9925,
        "sha256": "f5d94a2dff491cc5f6d8a6bb3869ea96e1abe7ac5b3a8125461e482a1feee039",
    },
    "computability/recursive-functions/sequences.tex": {
        "bytes": 8901,
        "sha256": "bb59145b1e2aaeb2129422762ffcc5695cf46f532b7114049cb555179bdd2ef8",
    },
    "turing-machines/undecidability/trakhtenbrot.tex": {
        "bytes": 14343,
        "sha256": "842bdfb7b060d3b09c37a16db8580825097d00d76e5c37c3ba56ed14b20ea1ac",
    },
    "incompleteness/arithmetization-syntax/proofs-in-lk.tex": {
        "bytes": 14072,
        "sha256": "4823606ada159ffd5e68e9b9680761b0674fec0a79cf3570fb2d58dea3c6d7cd",
    },
    "counterfactuals/minimal-change-semantics/antecedent-strengthening.tex": {
        "bytes": 3282,
        "sha256": "9012ee2fdb4513376bf00dab86743b4558f46a59b8234bf8123e7e099285e895",
    },
    "counterfactuals/minimal-change-semantics/transitivity.tex": {
        "bytes": 4684,
        "sha256": "0ca04f829161d135bc9501a5213f8fc699faee387130ef9e06fc242e4dea1a59",
    },
}
DOCUMENT_TEXT_SOURCE_IDENTITIES = {
    **EMPH_SOURCE_IDENTITIES,
    **LAYOUT_SOURCE_IDENTITIES,
}
RESIDUAL_VISUAL_TARGETS = {
    "OLVIS-0091": {"physical_pages": [164, 318], "source_lines": "103-106", "overflow_pt": 14.35321},
    "OLVIS-0133-OVERFLOW": {"physical_pages": [395], "source_lines": "74-79", "overflow_pt": 15.16975},
    "OLVIS-0133-COMMA": {"physical_pages": [395], "source_lines": "70", "visible_defect": r"t_{i+1},,\dots"},
    "OLVIS-0164": {"physical_pages": [253], "source_lines": "87-90", "overflow_pt": 12.78952},
    "OLVIS-0165": {"physical_pages": [256], "source_lines": "74-76", "overflow_pt": 15.11296},
    "OLVIS-0193": {"physical_pages": [553], "source_lines": "98-106", "overflow_pt": 25.47112},
    "OLVIS-0220": {"physical_pages": [598], "source_lines": "107-109", "overflow_pt": 10.07385},
    "OLVIS-0273": {"physical_pages": [674], "source_lines": "68-86", "overflow_pt": 17.6972},
    "OLVIS-0286": {"physical_pages": [695], "source_lines": "21-23", "overflow_pt": 21.58687},
    "OLVIS-0526": {"physical_pages": [1034], "source_lines": "33-44", "overflow_pt": 11.04391},
    "OLVIS-0527": {"physical_pages": [1035], "source_lines": "46-58", "overflow_pt": 11.04391},
}
EMERGENCY_STRETCH_RULES = {
    "OLVIS-0091": "15pt",
    "OLVIS-0193": "2em",
    "OLVIS-0220": "1em",
    "OLVIS-0286": "2em",
    "OLVIS-0526": "12pt",
    "OLVIS-0527": "12pt",
}
CENTERED_REFLOW_RULES = {
    "OLVIS-0133-OVERFLOW", "OLVIS-0164", "OLVIS-0165",
}
HISTORICAL_FIXTURE_OVERLAY_IDENTITY = {
    "path": "source/locale/fa-IR/standalone/source-corrections.tex",
    "bytes": 61699,
    "sha256": "9F9875F14DBCF20F6482CDC40F2EFF1787C6A084708EED154BE521D6C600AC60",
}
FIXTURE_RUNTIME_REFRESH = {
    "prior_runtime": {
        "bytes": 12907,
        "sha256": "2155DEE2F9762C6F58C4898811FCA07D8F42EEE45210B73D3E9A9A47CAFF31E8",
    },
    "current_runtime": {
        "bytes": 13186,
        "sha256": "6CB6D018AB461D185E5E2BCE71325649D0DBEE8BF52F8FA9BB3D736746EBDD58",
    },
    "prior_fixture": {
        "bytes": 7044,
        "sha256": "7BB9D8B2AD9DB83DF0C4C77FC07823DFD267DFF5E23DE1A8194028431AAC3179",
    },
    "current_fixture": {
        "bytes": 7044,
        "sha256": "10E1807B301424415C7FEAC2B663264CDA064DD75779DA0B3B3CBC99BCD564B5",
    },
}
OLVIS_0273_FAILED_DIAGNOSTIC = (
    ROOT
    / "tmp/pdfs/standalone/20260905T111918594Z-1e2ae9f475684383bbbe81c572bb0476"
)
OLVIS_0273_FAILED_DIAGNOSTIC_IDENTITIES = {
    "BUILD_RECEIPT.json": (
        6458, "36ff744d91cb0fefda8ddd5653f46517df2f5ce362754e9ef72d7fc8bd6a782f"
    ),
    "primary/open-logic-standalone-fa-IR.olcorrections": (
        1343, "c6dbf99661112da998f7f40893e2809488fa0a1eb2f621e86d8291a55f954b68"
    ),
    "primary/open-logic-standalone-fa-IR.log": (
        629030, "7673f83320970e9901f6d06358a380832e7cdc2b425bc6c1827bab12ec094151"
    ),
}
EXPECTED_NOTE_BODY_HASHES = {
    "OLP-0021": "f19c5adb7405f880264f2fac93aac9a0d59492673f2c794735264f471041b432",
    "OLP-0023": "061d1e73c35f4870ed0cbf5b966ee2158caa5fba2d06d90159ef7f937a82f061",
    "OLP-0024": "0a948dcc1f9512913fe5786d0e70a910c50e945fba161361c486e50701bee277",
    "OLP-0029": "185c10a88b50f336dbdbacddb6b0d361b4a59e09cc3cb9a8667a258c16dfad83",
    "OLP-0032": "f35bb99ab6a5b487ba80b2844b94906a12f8e21cb4b0f257b545aa053631bf95",
    "OLP-0034": "7575541c80057633fee733904649ec0a3170e81e1172ec06f8c19783d7a4efa1",
    "OLP-0035": "d9d6e575fd4e3b402fad340a408ed0401769af2e982d16939dd6ff414adb1bd2",
    "OLP-0036": "4078e96bc76230d82607e2698bc7e0bb2e493e7295eb728c39d801f8ba9ca43c",
    "OLP-0039": "78981d4bcc703617888b4d557bfc1c520312760e94251fe3cb03d25293d79d0e",
    "OLP-0040": "ae378c27c6ab3b1107cc239c0cac7238b663d420afb136065811049b5b6316c8",
}
EXPECTED_DEFERRED_NOTE_BODY_HASH = (
    "9c149dbb5661ee52325a13d67c4bceddfb1a942ca3f60d3788e1b2056b0ff858"
)
NATIVE_QA = ROOT / "evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_QA.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalized(text: str) -> str:
    return re.sub(r"\s", "", text)


def argument(text: str, offset: int) -> tuple[str, int]:
    while offset < len(text) and text[offset].isspace():
        offset += 1
    assert offset < len(text) and text[offset] == "{", (offset, text[offset:offset + 80])
    start = offset + 1
    depth = 1
    offset = start
    while depth:
        assert offset < len(text), "unterminated TeX argument"
        if text[offset] == "\\":
            offset += 2
            continue
        if text[offset] == "{":
            depth += 1
        elif text[offset] == "}":
            depth -= 1
        offset += 1
    return text[start:offset - 1], offset


def command_arguments(text: str, command: str, count: int) -> list[tuple[str, ...]]:
    rows: list[tuple[str, ...]] = []
    # Live declarations are control sequences at the start of a TeX line.
    # This excludes commented examples and the command's own definition while
    # accepting harmless spaces between the command and its first argument.
    pattern = re.compile(
        rf"(?m)^[ \t]*(?P<command>{re.escape(command)})(?=\s*\{{)"
    )
    for match in pattern.finditer(text):
        offset = match.end("command")
        args = []
        for _ in range(count):
            value, offset = argument(text, offset)
            args.append(value)
        rows.append(tuple(args))
    return rows


def active_tex(text: str) -> str:
    """Remove unescaped TeX comments while preserving line structure."""
    output = []
    for line in text.splitlines(keepends=True):
        comment_at = None
        for index, character in enumerate(line):
            if character != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                comment_at = index
                break
        if comment_at is None:
            output.append(line)
        else:
            newline = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
            output.append(line[:comment_at] + newline)
    return "".join(output)


def declarations(text: str) -> list[dict[str, str]]:
    return [
        {"unit": unit, "environment": environment, "rule": rule,
         "original": original, "replacement": replacement}
        for unit, environment, rule, original, replacement in command_arguments(
            text, r"\OLSADeclareSourceCorrection", 5
        )
    ]


def document_text_declarations(text: str) -> list[dict[str, str]]:
    return [
        {"unit": unit, "rule": rule, "original": original,
         "replacement": replacement}
        for unit, rule, original, replacement in command_arguments(
            text, r"\OLSADeclareDocumentTextCorrection", 4
        )
    ]


def check_derived_sources(rows: list[dict[str, str]]) -> dict[str, object]:
    """Independently reconstruct and verify every generated physical input."""
    manifest = json.loads(DERIVED_MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema"] == "farsi-standalone-derived-source-corrections/1.0.0"
    assert manifest["overlay_path"] == OVERLAY.relative_to(ROOT).as_posix()
    assert manifest["overlay_sha256"] == sha(OVERLAY)
    assert manifest["checker_path"] == Path(__file__).resolve().relative_to(ROOT).as_posix()
    assert manifest["checker_sha256"] == sha(Path(__file__).resolve())
    assert manifest["generator_path"] == DERIVED_GENERATOR.relative_to(ROOT).as_posix()
    assert manifest["generator_sha256"] == sha(DERIVED_GENERATOR)

    by_source: dict[Path, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        unit, environment, relative = DOCUMENT_TEXT_EXPECTED[row["rule"]]
        assert environment == "document-text" and unit == row["unit"]
        by_source[CONTENT_ROOT / relative].append(row)

    expected_paths = {"MANIFEST.json"}
    expected_records = []
    for source in sorted(by_source, key=lambda item: item.as_posix()):
        source_rows = by_source[source]
        unit = source_rows[0]["unit"]
        assert all(row["unit"] == unit for row in source_rows)
        source_bytes = source.read_bytes()
        has_bom = source_bytes.startswith(UTF8_BOM)
        corrected = (
            source_bytes[len(UTF8_BOM):].decode("utf-8")
            if has_bom else source_bytes.decode("utf-8")
        )
        rule_records = []
        for row in source_rows:
            assert corrected.count(row["original"]) == 1, row["rule"]
            corrected = corrected.replace(row["original"], row["replacement"], 1)
            rule_records.append({
                "finding_id": row["rule"],
                "original_sha256": text_sha(row["original"]),
                "replacement_sha256": text_sha(row["replacement"]),
            })
        terminal = r"\end{document}"
        assert corrected.count(terminal) == 1, source
        trace = (
            "% Standalone derived-source correction trace; generated, do not edit.\n"
            + "".join(
                f"\\OLSASourceCorrectionRecordDocumentText{{{unit}}}{{{row['rule']}}}\n"
                for row in source_rows
            )
        )
        corrected = corrected.replace(terminal, trace + terminal, 1)
        expected_bytes = (UTF8_BOM if has_bom else b"") + corrected.encode("utf-8")
        relative = source.relative_to(CONTENT_ROOT)
        derived = DERIVED_CONTENT / relative
        assert derived.read_bytes() == expected_bytes, derived
        relative_derived = derived.relative_to(ROOT).as_posix()
        expected_paths.add(derived.relative_to(DERIVED_ROOT).as_posix())
        expected_records.append({
            "source_id": unit,
            "source_path": source.relative_to(ROOT).as_posix(),
            "source_bytes": len(source_bytes),
            "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
            "derived_path": relative_derived,
            "derived_bytes": len(expected_bytes),
            "derived_sha256": hashlib.sha256(expected_bytes).hexdigest(),
            "utf8_bom_preserved": has_bom,
            "rules": rule_records,
        })

    assert manifest["source_files"] == len(expected_records)
    assert manifest["physical_correction_events"] == len(rows)
    assert manifest["files"] == expected_records
    actual_paths = {
        path.relative_to(DERIVED_ROOT).as_posix()
        for path in DERIVED_ROOT.rglob("*") if path.is_file()
    }
    assert actual_paths == expected_paths, {
        "missing": sorted(expected_paths - actual_paths),
        "unexpected": sorted(actual_paths - expected_paths),
    }
    return {
        "manifest_path": DERIVED_MANIFEST.relative_to(ROOT).as_posix(),
        "manifest_bytes": DERIVED_MANIFEST.stat().st_size,
        "manifest_sha256": sha(DERIVED_MANIFEST),
        "generator_path": DERIVED_GENERATOR.relative_to(ROOT).as_posix(),
        "generator_bytes": DERIVED_GENERATOR.stat().st_size,
        "generator_sha256": sha(DERIVED_GENERATOR),
        "derived_source_files": len(expected_records),
        "physical_correction_events": len(rows),
        "catcode_safe_native_file_input": True,
    }


def environment_bodies(text: str, environment: str) -> list[str]:
    begin = rf"\begin{{{environment}}}"
    end = rf"\end{{{environment}}}"
    bodies = []
    offset = 0
    while True:
        found = text.find(begin, offset)
        if found < 0:
            break
        body_start = found + len(begin)
        # Proof titles can contain nested optional arguments, for example
        # ``[... \olref[nen]{...} ...]``. A flat regex truncates that title.
        if body_start < len(text) and text[body_start] == "[":
            depth = 1
            cursor = body_start + 1
            while depth:
                assert cursor < len(text), f"unterminated optional title for {environment}"
                if text[cursor] == "[":
                    depth += 1
                elif text[cursor] == "]":
                    depth -= 1
                cursor += 1
            body_start = cursor
        body_end = text.find(end, body_start)
        assert body_end >= 0, f"unterminated {environment} environment"
        bodies.append(text[body_start:body_end])
        offset = body_end + len(end)
    return bodies


def math_spans(text: str) -> tuple[list[str], list[str]]:
    displays = [normalized(x) for x in re.findall(r"\\\[(.*?)\\\]", text, re.S)]
    without_displays = re.sub(r"\\\[.*?\\\]", "", text, flags=re.S)
    inlines = [normalized(x) for x in re.findall(r"(?<!\\)\$(.*?)(?<!\\)\$", without_displays, re.S)]
    return displays, inlines


def check_expected_overrides(text: str) -> list[tuple[str, str]]:
    overrides = command_arguments(text, r"\OLSASetSourceCorrectionExpected", 2)
    assert overrides == [("OLVIS-0091", "2")], overrides
    return overrides


def check_residual_ledger_contexts() -> dict[str, list[str]]:
    ledger = active_tex(GENERATED_LEDGER.read_text(encoding="utf-8"))
    rows = command_arguments(ledger, r"\OLSADeclareExpectedOrder", 1)
    assert len(rows) == 1
    entries = rows[0][0].split(",")
    expected = {
        "OLP-0091": ["PL", "FOL"],
        "OLP-0133": ["FOL"],
        "OLP-0164": ["FOL"],
        "OLP-0165": ["FOL"],
        "OLP-0193": ["FOL"],
        "OLP-0220": ["FOL"],
        "OLP-0273": ["FOL"],
        "OLP-0286": ["FOL"],
        "OLP-0526": ["FOL"],
        "OLP-0527": ["FOL"],
    }
    observed = {
        unit: [entry.split("/", 1)[1] for entry in entries if entry.startswith(unit + "/")]
        for unit in expected
    }
    assert observed == expected, observed
    return observed


def semantic_ids(rule: str) -> list[str]:
    return SPECIAL_RULE_TO_FINDINGS.get(rule, [rule])


def check_trace(
    text: str,
    expected_events: list[tuple[str, str, str, str]] = HISTORICAL_EXPECTED_EVENTS,
) -> list[tuple[str, str, str, str]]:
    lines = text.splitlines()
    assert lines and lines[0] == "source_id|environment|finding_id|occurrence"
    rows = [tuple(line.split("|")) for line in lines[1:] if line]
    assert all(len(row) == 4 for row in rows), rows
    assert rows == expected_events, (rows, expected_events)
    assert len(rows) == len(expected_events)
    # The same exact rule may legitimately recur with monotonically increasing
    # occurrences (OLVIS-0091), but an identical event row is never legitimate.
    assert len(rows) == len(set(rows))
    return rows


def check_log(
    text: str,
    expected_events: list[tuple[str, str, str, str]] = HISTORICAL_EXPECTED_EVENTS,
    expected_rule_count: int = len(EXPECTED_DECLARATIONS),
) -> list[tuple[str, str, str]]:
    hits = re.findall(
        r"^OL-STANDALONE-SOURCE-CORRECTION\|(OLP-\d{4})\|([^|]+)\|(\d+)$",
        text,
        re.M,
    )
    expected = [(unit, rule, occurrence) for unit, _env, rule, occurrence in expected_events]
    assert hits == expected, (hits, expected)
    coverage = re.findall(
        rf"^OL-STANDALONE-SOURCE-CORRECTION-COVERAGE\|{expected_rule_count}\|{expected_rule_count}$",
        text,
        re.M,
    )
    assert len(coverage) == 1, coverage
    return hits


def validate_olvis_0273_materialization_repair() -> dict[str, object]:
    """Bind the measured 39/40 failure and prove the repaired physical input."""
    for relative, identity in OLVIS_0273_FAILED_DIAGNOSTIC_IDENTITIES.items():
        path = OLVIS_0273_FAILED_DIAGNOSTIC / relative
        assert (path.stat().st_size, sha(path)) == identity, relative

    receipt_path = OLVIS_0273_FAILED_DIAGNOSTIC / "BUILD_RECEIPT.json"
    trace_path = (
        OLVIS_0273_FAILED_DIAGNOSTIC
        / "primary/open-logic-standalone-fa-IR.olcorrections"
    )
    log_path = (
        OLVIS_0273_FAILED_DIAGNOSTIC
        / "primary/open-logic-standalone-fa-IR.log"
    )
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    assert receipt["status"] == "FAILED"
    assert receipt["mutex"] == {
        "name": r"Global\InterlanguageTeXSlotV1",
        "acquired": True,
        "abandoned_recovery": False,
        "released_after_confirmed_tree_exit": True,
    }
    assert receipt["events"][-1]["kind"] == "worker_tree_exit"
    assert receipt["events"][-1]["details"]["result"]["ExitCode"] == 1

    expected_without_0273 = [
        event for event in CURRENT_EXPECTED_EVENTS if event[2] != "OLVIS-0273"
    ]
    observed = check_trace(
        trace_path.read_text(encoding="utf-8"), expected_without_0273
    )
    assert len(observed) == 39
    log_text = log_path.read_text(encoding="utf-8", errors="replace")
    log_hits = re.findall(
        r"^OL-STANDALONE-SOURCE-CORRECTION\|(OLP-\d{4})\|([^|]+)\|(\d+)$",
        log_text,
        re.M,
    )
    expected_log_hits = [
        (unit, rule, occurrence)
        for unit, _environment, rule, occurrence in expected_without_0273
    ]
    assert log_hits == expected_log_hits
    assert "Overfull \\hbox (17.6972pt too wide)" in log_text
    assert re.search(
        r"Wrong\s+event\s+count\s+for\s+OLP-0394\|lukasiewicz-name-source-ltr",
        log_text,
    )
    assert "OL-STANDALONE-SOURCE-CORRECTION-COVERAGE|" not in log_text

    derived = (
        DERIVED_CONTENT / "turing-machines/undecidability/trakhtenbrot.tex"
    )
    derived_text = derived.read_text(encoding="utf-8")
    assert "، و\\linebreak\n" in derived_text
    assert derived_text.count(r"\linebreak") == 1
    assert derived_text.count(
        r"\OLSASourceCorrectionRecordDocumentText{OLP-0273}{OLVIS-0273}"
    ) == 1
    return {
        "status": "PASS_MEASURED_FAILURE_BOUND_AND_PRE_SERIALIZATION_REPAIR_STATICALLY_VERIFIED",
        "failed_diagnostic": {
            "receipt": receipt_path.relative_to(ROOT).as_posix(),
            "receipt_bytes": receipt_path.stat().st_size,
            "receipt_sha256": sha(receipt_path),
            "trace": trace_path.relative_to(ROOT).as_posix(),
            "trace_bytes": trace_path.stat().st_size,
            "trace_sha256": sha(trace_path),
            "observed_events": len(observed),
            "missing_event": "OLP-0273|document-text|OLVIS-0273|1",
            "log": log_path.relative_to(ROOT).as_posix(),
            "log_bytes": log_path.stat().st_size,
            "log_sha256": sha(log_path),
            "measured_overflow_pt": 17.6972,
            "unrelated_terminal_failure": "OLP-0394 bidi-layout expected-count mismatch",
            "captured_tree_drained_and_mutex_released": True,
        },
        "repair": {
            "policy": "exact source fragment materialized before answers.sty serialization",
            "derived_path": derived.relative_to(ROOT).as_posix(),
            "derived_bytes": derived.stat().st_size,
            "derived_sha256": sha(derived),
            "replacement_linebreak_count": 1,
            "trace_record_count": 1,
            "next_guarded_build_required": True,
        },
    }


def resolve_artifact(path: Path) -> Path:
    return path.resolve() if path.is_absolute() else (ROOT / path).resolve()


def assert_record_identity(record: dict[str, object]) -> Path:
    path = resolve_artifact(Path(str(record["path"])))
    assert path.is_file(), path
    assert sha(path).lower() == str(record["sha256"]).lower(), path
    if "bytes" in record:
        assert path.stat().st_size == int(record["bytes"]), path
    return path


def check_activation_topology(
    body_text: str, runtime_text: str, driver_text: str
) -> dict[str, object]:
    body = active_tex(body_text)
    body_inputs = [row[0] for row in command_arguments(body, r"\input", 1)]
    assert body_inputs == [
        "standalone/runtime-fixes.tex",
        "standalone/link-geometry.tex",
        "standalone/runtime.tex",
        "standalone/generated-ledger.tex",
        "standalone/context.tex",
        "standalone/source-corrections.tex",
        "standalone/typography.tex",
        "standalone/bidi-layout.tex",
        "standalone/variants.tex",
    ]
    assert command_arguments(body, r"\InputIfFileExists", 3) == [
        ("standalone-errata.tex", "", "")
    ]
    assert len(re.findall(r"(?m)^[ \t]*\\OLSAStart[ \t]*$", body)) == 1
    assert len(re.findall(r"(?m)^[ \t]*\\OLSAVerify[ \t]*$", body)) == 1
    ordered_tokens = [
        r"\input{standalone/runtime-fixes.tex}",
        r"\input{standalone/link-geometry.tex}",
        r"\input{standalone/runtime.tex}",
        r"\input{standalone/generated-ledger.tex}",
        r"\input{standalone/context.tex}",
        r"\input{standalone/source-corrections.tex}",
        r"\input{standalone/typography.tex}",
        r"\input{standalone/bidi-layout.tex}",
        r"\InputIfFileExists{standalone-errata.tex}{}{}",
        r"\OLSAStart",
        r"\input{standalone/variants.tex}",
        r"\OLSAVerify",
    ]
    positions = [body.index(token) for token in ordered_tokens]
    assert positions == sorted(positions)

    driver = active_tex(driver_text)
    driver_inputs = [row[0] for row in command_arguments(driver, r"\input", 1)]
    assert driver_inputs.count("standalone/body.tex") == 1
    body_position = driver.index(r"\input{standalone/body.tex}")
    assert driver.index(r"\begin{document}") < body_position < driver.index(r"\end{document}")

    runtime = normalized(active_tex(runtime_text))
    start_hook = r"\cs_if_exist:NT\OLSASourceCorrectionsStart{\OLSASourceCorrectionsStart}"
    verify_hook = r"\cs_if_exist:NT\OLSASourceCorrectionsVerify{\OLSASourceCorrectionsVerify}"
    assert runtime.count(start_hook) == 1
    assert runtime.count(verify_hook) == 1
    return {
        "body_inputs": body_inputs,
        "errata_loader": "standalone-errata.tex",
        "driver_body_input_count": driver_inputs.count("standalone/body.tex"),
        "runtime_start_hook_count": runtime.count(start_hook),
        "runtime_verify_hook_count": runtime.count(verify_hook),
    }


def validate_audits() -> list[dict[str, object]]:
    for path, expected_hash in AUDIT_HASHES.items():
        assert sha(path) == expected_hash, path
    functions = json.loads(AUDIT_FINDINGS_FUNCTIONS.read_text(encoding="utf-8"))
    assert functions["schema"] == "openlogic-shared-source-audit/1"
    assert functions["audit_id"] == AUDIT_IDS[0]
    assert [row["id"] for row in functions["findings"]] == FUNCTION_FINDINGS
    assert functions["external_upstream_report_submitted"] is False
    size = json.loads(AUDIT_FINDINGS_SIZE.read_text(encoding="utf-8"))
    assert size["schema"] == "openlogic-shared-source-audit/1.0.0"
    assert size["audit_id"] == AUDIT_IDS[1]
    assert [row["finding_id"] for row in size["findings"]] == SIZE_FINDINGS
    assert size["scope"]["finding_count"] == len(SIZE_FINDINGS)
    retraction = json.loads(AUDIT_RETRACTION.read_text(encoding="utf-8"))
    assert retraction["schema"] == "openlogic-shared-source-finding-retraction/1"
    assert retraction["status"] == "FINAL_RETRACTION_FALSE_POSITIVE"
    assert retraction["correct_byte_evidence"]["source_defect"] is False
    assert retraction["required_lane_action"].startswith("Do not apply")
    assert retraction["external_upstream_issue_submitted"] is False
    tombstone = json.loads(AUDIT_TOMBSTONE.read_text(encoding="utf-8"))
    assert tombstone["audit_id"] == "OLSIZ-011"
    assert tombstone["parent_audit_id"] == AUDIT_IDS[1]
    assert tombstone["status"] == "RETRACTED_FALSE_POSITIVE_DO_NOT_APPLY"
    assert tombstone["byte_recheck"]["backslash_count_before_hline"] == 3
    assert tombstone["byte_recheck"]["invalid_two_backslashes_then_literal_hline_occurrences"] == 0
    assert tombstone["external_upstream_issue_submitted"] is False
    return [
        {"path": str(path), "bytes": path.stat().st_size, "sha256": expected_hash}
        for path, expected_hash in AUDIT_HASHES.items()
    ]


def validate_fixture(source_files: dict[str, Path]) -> dict[str, object]:
    fixture_bytes = FIXTURE.read_bytes()
    current_fixture = FIXTURE_RUNTIME_REFRESH["current_fixture"]
    assert len(fixture_bytes) == current_fixture["bytes"]
    assert hashlib.sha256(fixture_bytes).hexdigest().upper() == current_fixture["sha256"]
    current_runtime = FIXTURE_RUNTIME_REFRESH["current_runtime"]
    prior_runtime = FIXTURE_RUNTIME_REFRESH["prior_runtime"]
    current_size_token = f'"bytes": {current_runtime["bytes"]}'.encode("ascii")
    prior_size_token = f'"bytes": {prior_runtime["bytes"]}'.encode("ascii")
    current_hash_token = str(current_runtime["sha256"]).encode("ascii")
    prior_hash_token = str(prior_runtime["sha256"]).encode("ascii")
    assert fixture_bytes.count(current_size_token) == 1
    assert fixture_bytes.count(current_hash_token) == 1
    reconstructed_prior = fixture_bytes.replace(
        current_size_token, prior_size_token, 1
    ).replace(current_hash_token, prior_hash_token, 1)
    prior_fixture = FIXTURE_RUNTIME_REFRESH["prior_fixture"]
    assert len(reconstructed_prior) == prior_fixture["bytes"]
    assert hashlib.sha256(reconstructed_prior).hexdigest().upper() == prior_fixture["sha256"]
    fixture = json.loads(fixture_bytes.decode("utf-8"))
    assert fixture["schema"] == "farsi-combined-source-corrections-probe-fixture-v5"
    assert fixture["audit_ids"] == AUDIT_IDS
    assert fixture["physical_rules"] == [row[2] for row in EXPECTED_DECLARATIONS]
    assert fixture["physical_rule_count"] == len(EXPECTED_DECLARATIONS) == 15
    assert fixture["semantic_finding_count"] == len(SEMANTIC_FINDINGS) == 15
    assert fixture["rule_to_findings"] == SPECIAL_RULE_TO_FINDINGS
    assert fixture["expected_trace_events"] == 15
    assert fixture["deferred_problem_rule"] == "OLSIZ-002"
    assert fixture["tex_run"] is False and fixture["not_full_reader"] is True
    for key, path in {"runtime": RUNTIME, "errata": ERRATA}.items():
        assert fixture["dependencies"][key] == {
            "path": path.relative_to(ROOT).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha(path).upper(),
        }
    # The accepted native probe is immutable historical evidence for the first
    # 15 events. The current overlay is intentionally additive and therefore
    # must not be substituted into that old probe's dependency record.
    assert fixture["dependencies"]["overlay"] == HISTORICAL_FIXTURE_OVERLAY_IDENTITY
    marker = b"\\begin{document}"
    driver_bytes = DRIVER.read_bytes()
    assert driver_bytes.count(marker) == 1
    preamble_bytes = driver_bytes[:driver_bytes.index(marker) + len(marker)]
    preamble = fixture["driver_preamble"]
    assert preamble == {
        "path": DRIVER.relative_to(ROOT).as_posix(),
        "boundary": r"\begin{document}",
        "boundary_inclusive": True,
        "bytes": len(preamble_bytes),
        "sha256": hashlib.sha256(preamble_bytes).hexdigest().upper(),
    }
    continuity = fixture["historical_evidence_continuity"]
    assert continuity["status"] == "PASS_PREAMBLE_AND_PROBE_TEX_BYTES_UNCHANGED"
    assert continuity["preamble_bytes_unchanged"] is True
    assert continuity["probe_tex_bytes_unchanged"] is True
    assert continuity["post_boundary_driver_changes_out_of_scope"] is True
    assert continuity["historical_driver_preamble"] == {
        "boundary": r"\begin{document}",
        "boundary_inclusive": True,
        "bytes": len(preamble_bytes),
        "sha256": hashlib.sha256(preamble_bytes).hexdigest().upper(),
    }
    assert continuity["historical_full_driver_locator_only"] == {
        "path": DRIVER.relative_to(ROOT).as_posix(),
        "bytes": 13343,
        "sha256": "F983E663C874FCEE8B2065E15FFCA1B3AB7C08174FA5EC970B7E96366E2C05D2",
    }
    continuity_files = {
        "accepted_probe_tex": ROOT / "source/locale/fa-IR/standalone-probe-source-corrections.tex",
        "accepted_native_qa": ROOT / "evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_QA.json",
        "accepted_complete_visual_qa": ROOT / "evidence/SOURCE_CORRECTIONS_NATIVE_PROBE_VISUAL_QA.json",
    }
    for key, path in continuity_files.items():
        assert continuity[key] == {
            "path": path.relative_to(ROOT).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha(path).upper(),
        }
    native = json.loads(NATIVE_QA.read_text(encoding="utf-8"))
    assert native["schema"] == "farsi-combined-source-corrections-native-probe-qa-v3"
    assert native["status"].startswith("PASS_NATIVE_DIAGNOSTIC")
    receipt_path = assert_record_identity({
        "path": native["guarded_run"]["receipt_path"],
        "sha256": native["guarded_run"]["receipt_sha256"],
    })
    native_artifacts = {
        key: assert_record_identity(record)
        for key, record in native["artifacts"].items()
    }
    trace_path = assert_record_identity({
        "path": native["trace"]["path"],
        "sha256": native["trace"]["sha256"],
    })
    source_inventory_path = assert_record_identity({
        "path": native["guarded_run"]["source_inventory"]["path"],
        "sha256": native["guarded_run"]["source_inventory"]["sha256"],
    })
    probe = continuity_files["accepted_probe_tex"]
    assert fixture["output"] == {
        "path": probe.relative_to(ROOT).as_posix(),
        "sha256": sha(probe).upper(),
        "bytes": probe.stat().st_size,
    }
    expected_units = []
    seen_units: set[str] = set()
    for unit, _environment, _rule, _relative in EXPECTED_DECLARATIONS:
        if unit in seen_units:
            continue
        seen_units.add(unit)
        source = source_files[unit]
        expected_units.append({
            "path": source.relative_to(ROOT).as_posix(),
            "bytes": source.stat().st_size,
            "sha256": sha(source).upper(),
            "unit_id": unit,
        })
    assert fixture["source_units"] == expected_units
    return {
        "path": FIXTURE.relative_to(ROOT).as_posix(),
        "bytes": FIXTURE.stat().st_size,
        "sha256": sha(FIXTURE),
        "schema": fixture["schema"],
        "accepted_native_receipt": receipt_path.relative_to(ROOT).as_posix(),
        "accepted_native_artifacts": {
            key: path.relative_to(ROOT).as_posix()
            for key, path in native_artifacts.items()
        },
        "accepted_native_trace": trace_path.relative_to(ROOT).as_posix(),
        "accepted_source_inventory": source_inventory_path.relative_to(ROOT).as_posix(),
        "runtime_dependency_refresh": {
            **FIXTURE_RUNTIME_REFRESH,
            "only_runtime_dependency_bytes_changed": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace-file", type=Path, required=True)
    parser.add_argument("--trace-log", type=Path, required=True)
    parser.add_argument("--write-evidence", action="store_true")
    args = parser.parse_args()

    assert sha(STAGING) == STAGING_SHA256
    manifest = json.loads(STAGING.read_text(encoding="utf-8"))
    assert len(manifest["files"]) == 828
    drift = []
    for row in manifest["files"]:
        path = ROOT / row["path"]
        if path.stat().st_size != row["bytes"] or sha(path) != row["sha256"]:
            drift.append(row["path"])
    assert not drift, drift

    audit_evidence = validate_audits()
    overlay_text = OVERLAY.read_text(encoding="utf-8")
    rows = declarations(overlay_text)
    expected_headers = [
        (unit, environment, rule)
        for unit, environment, rule, _relative in SOURCE_EXPECTED_DECLARATIONS
    ]
    assert [(row["unit"], row["environment"], row["rule"]) for row in rows] == expected_headers
    assert len(rows) == len({row["rule"] for row in rows}) == 15
    assert expected_headers == [
        (unit, environment, rule)
        for unit, environment, rule, _relative in EXPECTED_DECLARATIONS
    ]
    document_text_rows = document_text_declarations(overlay_text)
    expected_document_text_headers = [
        (unit, rule)
        for unit, _environment, rule, _relative in DOCUMENT_TEXT_EXPECTED_DECLARATIONS
    ]
    assert [(row["unit"], row["rule"]) for row in document_text_rows] == expected_document_text_headers
    assert len(document_text_rows) == len({row["rule"] for row in document_text_rows}) == 24
    assert expected_document_text_headers[:13] == [
        (unit, rule)
        for unit, _environment, rule, _relative in (
            EMPH_EXPECTED_DECLARATIONS + LAYOUT_EXPECTED_DECLARATIONS[:6]
        )
    ]
    all_rule_names = [row["rule"] for row in rows + document_text_rows]
    assert len(all_rule_names) == len(set(all_rule_names)) == 39
    assert len(CURRENT_EXPECTED_EVENTS) == 40
    assert PRIOR_EXACT_RULE_COUNT == PRIOR_RUNTIME_EVENT_COUNT == 28
    assert all(audit_id in overlay_text for audit_id in AUDIT_IDS)
    assert all(family in overlay_text for family in DOCUMENT_TEXT_REPAIR_FAMILIES)
    assert "OLSIZ-011" not in overlay_text
    active_overlay = active_tex(overlay_text)
    normalized_overlay = normalized(active_overlay)
    assert r"\NewDocumentCommand\OLSADeclareSourceCorrection{mmm+m+m}" in normalized_overlay
    # Whole-document macro/xparse collection pre-tokenizes answers.sty's
    # deferred problems and verbatim-style input under the wrong catcodes.
    # Require normal file input from independently verified derived sources.
    for forbidden in (
        r"\olsa_source_correction_collect_document_text:w",
        r"\olsa_source_correction_document_text:nn",
        r"\RenewDocumentCommand\olsection",
        r"\l_olsa_source_correction_document_accum_tl",
    ):
        assert forbidden not in normalized_overlay
    assert normalized_overlay.count(
        r"\NewDocumentCommand\OLSASourceCorrectionRecordDocumentText{mm}"
    ) == 1
    assert normalized_overlay.count(
        r"\tl_set:Nx\l_olsa_path_tl{standalone/generated-source-corrections/\OLStandaloneCurrentPath}"
    ) == 1

    setup_rows = command_arguments(overlay_text, r"\OLSADeclareSetup", 2)
    expected_setups = [
        ("OLP-0021", r"\olsa_source_correction_install_ex:"),
        ("OLP-0023", r"\olsa_source_correction_install_explain:"),
        ("OLP-0024", r"\olsa_source_correction_install_prop:\olsa_source_correction_install_proof:"),
        ("OLP-0029", r"\olsa_source_correction_install_ex:"),
        ("OLP-0032", r"\olsa_source_correction_install_explain:"),
        ("OLP-0034", r"\olsa_source_correction_install_proof:\olsa_source_correction_install_explain:"),
        ("OLP-0035", r"\olsa_source_correction_install_proof:"),
        ("OLP-0036", r"\olsa_source_correction_install_proof:"),
        ("OLP-0039", r"\olsa_source_correction_install_proof:"),
        ("OLP-0040", r"\olsa_source_correction_install_proof:"),
        ("OLP-0179", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0180", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0362", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0379", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0391", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0569", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0570", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0599", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0091", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0133", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0164", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0165", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0193", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0220", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0273", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0286", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0526", r"\olsa_source_correction_install_document_text:"),
        ("OLP-0527", r"\olsa_source_correction_install_document_text:"),
    ]
    assert [(unit, normalized(active_tex(body))) for unit, body in setup_rows] == expected_setups
    assert len(re.findall(
        r"(?m)^[ \t]*\\olsa_source_correction_install_probdeferred:[ \t]*$",
        active_overlay,
    )) == 1
    assert normalized(active_overlay).count(
        r"\NewDocumentCommand\OLSADeclareDocumentTextCorrection{mm+m+m}"
    ) == 1
    assert normalized(active_overlay).count(
        r"\NewDocumentCommand\OLSASetSourceCorrectionExpected{mm}"
    ) == 1
    expected_overrides = check_expected_overrides(overlay_text)
    override_token = r"\OLSASetSourceCorrectionExpected{OLVIS-0091}{2}"
    assert overlay_text.count(override_token) == 1
    for mutation in (
        override_token.replace("{2}", "{3}"),
        override_token.replace("OLVIS-0091", "OLVIS-0133-OVERFLOW"),
    ):
        mutated_overlay = overlay_text.replace(override_token, mutation, 1)
        try:
            check_expected_overrides(mutated_overlay)
        except AssertionError:
            pass
        else:
            raise AssertionError("mutated correction expected-count override accepted")
    assert r"\NewCommandCopy\olsa_source_correction_original_olsection\olsection" not in normalized(active_overlay)
    assert normalized(active_overlay).count(
        r"\NewDocumentCommand\OLSASourceCorrectionRecordDocumentText{mm}"
    ) == 1
    assert "{#1|document-text|#2|\\l_olsa_source_correction_count_tl}" in normalized(active_overlay)
    residual_ledger_contexts = check_residual_ledger_contexts()
    olvis_0273_repair_evidence = validate_olvis_0273_materialization_repair()

    source_cache: dict[Path, str] = {}
    source_files: dict[str, Path] = {}
    results = []
    mapped_semantic_counts: Counter[str] = Counter()
    for row in rows:
        unit, environment, relative = EXPECTED[row["rule"]]
        assert (row["unit"], row["environment"]) == (unit, environment)
        source = SOURCE_ROOT / relative
        source_files[unit] = source
        source_text = source_cache.setdefault(source, source.read_text(encoding="utf-8-sig"))
        bodies = environment_bodies(source_text, environment)
        matched_bodies = [
            body for body in bodies if normalized(body) == normalized(row["original"])
        ]
        hits = len(matched_bodies)
        assert hits == 1, (row["rule"], hits)
        mutated_original = row["original"] + "OLSA-MUTATION-SENTINEL"
        assert not any(
            normalized(body) == normalized(mutated_original) for body in bodies
        )
        assert sum(
            normalized(body) == normalized(row["original"])
            for body in bodies + [row["original"]]
        ) == 2
        assert normalized(row["original"]) != normalized(row["replacement"])
        original_hash = text_sha(row["original"])
        replacement_hash = text_sha(row["replacement"])
        assert (original_hash, replacement_hash) == EXPECTED_BODY_HASHES[row["rule"]], row["rule"]
        old_displays, old_inline = math_spans(row["original"])
        new_displays, new_inline = math_spans(row["replacement"])
        finding_ids = (
            [row["rule"]]
            if row["rule"] in RESIDUAL_ADDITIONAL_FINDINGS
            else semantic_ids(row["rule"])
        )
        mapped_semantic_counts.update(finding_ids)
        results.append({
            "physical_rule": row["rule"], "semantic_findings": finding_ids,
            "unit": unit, "environment": environment,
            "source_path": source.relative_to(ROOT).as_posix(),
            "source_bytes": source.stat().st_size, "source_sha256": sha(source),
            "whitespace_normalized_source_body_hits": hits,
            "matched_source_environment_body_sha256": text_sha(matched_bodies[0]),
            "overlay_original_body_sha256": original_hash,
            "replacement_body_sha256": replacement_hash,
            "original_display_math_spans": len(old_displays),
            "replacement_display_math_spans": len(new_displays),
            "original_inline_math_spans": len(old_inline),
            "replacement_inline_math_spans": len(new_inline),
        })
    assert mapped_semantic_counts == EXPECTED_SEMANTIC_MAPPING_COUNTS

    document_text_results = []
    document_text_source_files: dict[str, Path] = {}
    repaired_source_text: dict[Path, str] = {}
    document_selector_evidence: dict[str, dict[str, object]] = {}
    document_tails: dict[str, str] = {}
    typography_units = {
        unit for unit, _rule, _punctuation, _formula in command_arguments(
            TYPOGRAPHY.read_text(encoding="utf-8"), r"\OLSADeclareDisplay", 4
        )
    }
    target_document_units = {row[0] for row in DOCUMENT_TEXT_EXPECTED_DECLARATIONS}
    assert target_document_units.isdisjoint(typography_units)
    for row in document_text_rows:
        unit, environment, relative = DOCUMENT_TEXT_EXPECTED[row["rule"]]
        assert row["unit"] == unit and environment == "document-text"
        source = CONTENT_ROOT / relative
        document_text_source_files[unit] = source
        identity = DOCUMENT_TEXT_SOURCE_IDENTITIES[relative]
        assert source.stat().st_size == identity["bytes"]
        assert sha(source) == identity["sha256"]
        source_text = source_cache.setdefault(source, source.read_text(encoding="utf-8-sig"))
        active_source = active_tex(source_text)
        if unit not in document_selector_evidence:
            section_markers = list(re.finditer(r"(?m)^[ \t]*\\olsection(?=\s*(?:\[|\{))", active_source))
            assert len(section_markers) == 1
            assert active_source.count(r"\end{document}") == 1
            end_position = active_source.index(r"\end{document}")
            assert section_markers[0].end() < end_position
            document_tails[unit] = active_source[section_markers[0].end():end_position]
            document_selector_evidence[unit] = {
                "source_path": source.relative_to(ROOT).as_posix(),
                "olsection_markers": len(section_markers),
                "terminal_document_markers": active_source.count(r"\end{document}"),
                "selector_scope": "exact-source-fragment-in-hash-bound-derived-physical-input",
                "typography_active_dollar_overlap": False,
            }
        tail = document_tails[unit]
        raw_hits = tail.count(row["original"])
        normalized_hits = normalized(tail).count(normalized(row["original"]))
        assert raw_hits == normalized_hits == 1, (
            row["rule"], raw_hits, normalized_hits
        )
        mutated_original = row["original"] + "OLSA-MUTATION-SENTINEL"
        assert normalized(tail).count(normalized(mutated_original)) == 0
        assert normalized(tail + row["original"]).count(
            normalized(row["original"])
        ) == 2
        if row["rule"] in EMPH_FINDINGS:
            assert row["replacement"] == row["original"].replace("emph{", r"\emph{", 1)
            assert row["original"].count("emph{") == 1
            assert row["replacement"].count(r"\emph{") == 1
        else:
            assert row["rule"] in LAYOUT_FINDINGS
            if row["rule"] in LAYOUT_FINDINGS[:6]:
                assert row["original"].count(r"\linebreak") == 0
                assert row["replacement"].count(r"\linebreak") == 1
                stripped = row["replacement"].replace(r"\linebreak", "", 1)
                stripped_normalized = normalized(stripped)
                original_normalized = normalized(row["original"])
                if row["rule"] in LINEBREAK_REPLACES_TIE_FINDINGS:
                    # These three interventions replace the exact nonbreaking
                    # tie at the new break point.  The pinned body hashes below
                    # prevent this narrowly allowed deletion from masking any
                    # other source change.
                    assert stripped_normalized == original_normalized.replace("~", "", 1), row["rule"]
                else:
                    assert stripped_normalized == original_normalized, row["rule"]
            elif row["rule"] == "OLVIS-0273":
                assert row["original"].count(r"\linebreak") == 0
                assert row["replacement"].count(r"\linebreak") == 1
                assert normalized(
                    row["replacement"].replace(r"\linebreak", "", 1)
                ) == normalized(row["original"])
                assert "، و\\linebreak" in row["replacement"]
            elif row["rule"] == "OLVIS-0133-COMMA":
                malformed = r"t_{i+1},,\dots"
                corrected = r"t_{i+1},\dots"
                assert row["original"].count(malformed) == 1
                assert row["replacement"] == row["original"].replace(
                    malformed, corrected, 1
                )
                assert malformed not in row["replacement"]
                formula_mutation = row["replacement"].replace(
                    "t_{i+1}", "t_{i+2}", 1
                )
                assert formula_mutation != row["original"].replace(
                    malformed, corrected, 1
                )
            elif row["rule"] in CENTERED_REFLOW_RULES:
                assert row["original"].count(r"\begin{center}") == 0
                assert row["replacement"].count(r"\begin{center}") == 1
                assert row["replacement"].count(r"\end{center}") == 1
                stripped = row["replacement"].replace(
                    r"\begin{center}", "", 1
                ).replace(r"\end{center}", "", 1)
                assert normalized(stripped) == normalized(row["original"])
            else:
                stretch = EMERGENCY_STRETCH_RULES[row["rule"]]
                marker = "{\\emergencystretch=" + stretch + r"\relax"
                assert row["original"].count(r"\emergencystretch") == 0
                assert row["replacement"].count(marker) == 1
                assert row["replacement"].count(r"\par}") == 1
                stripped = row["replacement"].replace(marker, "", 1).replace(
                    r"\par}", "", 1
                )
                assert normalized(stripped) == normalized(row["original"])
            if row["rule"] != "OLVIS-0133-COMMA":
                assert math_spans(row["original"]) == math_spans(row["replacement"])
        original_hash = text_sha(row["original"])
        replacement_hash = text_sha(row["replacement"])
        assert (original_hash, replacement_hash) == DOCUMENT_TEXT_EXPECTED_BODY_HASHES[row["rule"]]
        current = repaired_source_text.setdefault(source, source_text)
        assert current.count(row["original"]) == 1
        assert normalized(current).count(normalized(row["original"])) == 1
        repaired_source_text[source] = current.replace(row["original"], row["replacement"], 1)
        document_text_results.append({
            "physical_rule": row["rule"],
            "semantic_findings": [row["rule"]],
            "unit": unit,
            "environment": environment,
            "source_path": source.relative_to(ROOT).as_posix(),
            "source_bytes": source.stat().st_size,
            "source_sha256": sha(source),
            "exact_source_fragment_hits": raw_hits,
            "whitespace_normalized_source_fragment_hits": normalized_hits,
            "overlay_original_fragment_sha256": original_hash,
            "replacement_fragment_sha256": replacement_hash,
        })
        mapped_semantic_counts.update([row["rule"]])
    emph_rows = [row for row in document_text_rows if row["rule"] in EMPH_FINDINGS]
    assert sum(
        len(re.findall(r"(?<!\\)\bemph\{", repaired_source_text[CONTENT_ROOT / relative]))
        for relative in EMPH_SOURCE_IDENTITIES
    ) == 0
    assert sum(
        int(identity["malformed_emph_occurrences"])
        for identity in EMPH_SOURCE_IDENTITIES.values()
    ) == len(emph_rows) == 7
    for relative, identity in EMPH_SOURCE_IDENTITIES.items():
        source = CONTENT_ROOT / relative
        source_text = source_cache[source]
        assert len(re.findall(r"(?<!\\)\bemph\{", source_text)) == identity["malformed_emph_occurrences"]
    assert mapped_semantic_counts == (
        EXPECTED_SEMANTIC_MAPPING_COUNTS + Counter(DOCUMENT_TEXT_FINDINGS)
    )
    derived_source_evidence = check_derived_sources(document_text_rows)

    by_rule = {row["rule"]: row for row in rows}
    assert "نامنفی" in by_rule["OLFUN-002"]["replacement"]
    assert "ریشهٔ اصلی" in by_rule["OLFUN-002"]["replacement"]
    assert "طبیعی~$x$" in by_rule["OLFUN-003"]["replacement"]
    assert "طبیعی~$n$" not in by_rule["OLFUN-003"]["replacement"]
    assert "رابطه‌ای میان $A$ و~$B$" in by_rule["OLFUN-004"]["replacement"]
    assert "رابطه‌ای روی $A" not in by_rule["OLFUN-004"]["replacement"]
    assert "همانندی‌ای" in by_rule["OLFUN-005"]["replacement"]
    assert "اگر $A$ ناتهی باشد" in by_rule["OLFUN-001-THEOREM"]["replacement"]
    assert "عنصری\n  $a \\in A$ برگزینید" in by_rule["OLFUN-001-PROOF"]["replacement"]

    fixture_evidence = validate_fixture(source_files)
    errata = ERRATA.read_text(encoding="utf-8")
    assert "OLSIZ-011" not in errata
    after = command_arguments(errata, r"\OLSADeclareAfter", 2)
    deferred = command_arguments(errata, r"\OLSADeclareDeferredCorrectionAfter", 2)
    note_bindings = {
        "OLP-0021": ["OLFUN-002", "OLFUN-003"],
        "OLP-0023": ["OLFUN-004", "OLFUN-005"],
        "OLP-0024": ["OLFUN-001"],
        "OLP-0029": ["OLSIZ-001"],
        "OLP-0032": ["OLSIZ-003"],
        "OLP-0034": ["OLSIZ-004", "OLSIZ-005"],
        "OLP-0035": ["OLSIZ-006"],
        "OLP-0036": ["OLSIZ-007"],
        "OLP-0039": ["OLSIZ-008", "OLSIZ-009"],
        "OLP-0040": ["OLSIZ-010"],
    }
    expected_note_units = list(note_bindings)
    expected_note_set = set(expected_note_units)
    assert [unit for unit, _body in after if unit in expected_note_set] == expected_note_units
    for unit, expected_ids in note_bindings.items():
        bodies = [active_tex(note_body) for note_unit, note_body in after if note_unit == unit]
        assert len(bodies) == 1, unit
        observed_ids = [
            finding_id for finding_id in SEMANTIC_FINDINGS
            if bodies[0].count(finding_id) == 1
        ]
        assert observed_ids == [finding for finding in SEMANTIC_FINDINGS if finding in expected_ids], unit
        assert all(bodies[0].count(finding_id) == 0 for finding_id in SEMANTIC_FINDINGS if finding_id not in expected_ids)
        assert text_sha(bodies[0]) == EXPECTED_NOTE_BODY_HASHES[unit], unit
    assert len(deferred) == 1 and deferred[0][0] == "OLSIZ-002"
    deferred_body = active_tex(deferred[0][1])
    assert deferred_body.count("OLSIZ-002") == 1
    assert all(deferred_body.count(finding_id) == 0 for finding_id in SEMANTIC_FINDINGS if finding_id != "OLSIZ-002")
    assert text_sha(deferred_body) == EXPECTED_DEFERRED_NOTE_BODY_HASH
    assert not any(unit == "OLP-0031" for unit, _body in after)

    activation_evidence = check_activation_topology(
        BODY.read_text(encoding="utf-8"),
        RUNTIME.read_text(encoding="utf-8"),
        DRIVER.read_text(encoding="utf-8"),
    )
    body = active_tex(BODY.read_text(encoding="utf-8"))
    assert body.index(r"\input{standalone/context.tex}") < body.index(
        r"\input{standalone/source-corrections.tex}"
    ) < body.index(r"\input{standalone/typography.tex}") < body.index(r"\OLSAStart")
    runtime = active_tex(RUNTIME.read_text(encoding="utf-8"))
    assert r"\cs_if_exist:NT \OLSASourceCorrectionsStart {\OLSASourceCorrectionsStart}" in runtime
    assert r"\cs_if_exist:NT \OLSASourceCorrectionsVerify {\OLSASourceCorrectionsVerify}" in runtime
    assert "{#2}" in overlay_text
    assert "OL-STANDALONE-SOURCE-CORRECTION-COVERAGE" in overlay_text
    assert r"\RenewDocumentEnvironment{probdeferred}{m +b}" in overlay_text
    assert r"\OLSADeclareDeferredCorrectionAfter" in overlay_text

    valid_trace = "source_id|environment|finding_id|occurrence\n" + "\n".join(
        "|".join(event) for event in CURRENT_EXPECTED_EVENTS
    ) + "\n"
    check_trace(valid_trace, CURRENT_EXPECTED_EVENTS)
    occurrence_two = "OLP-0091|document-text|OLVIS-0091|2\n"
    assert valid_trace.count(occurrence_two) == 1
    for invalid in (
        "\n".join(valid_trace.splitlines()[:-1]) + "\n",
        valid_trace + valid_trace.splitlines()[1] + "\n",
        valid_trace.replace("|1\n", "|2\n", 1),
        valid_trace.replace("OLP-0021", "OLP-9999", 1),
        valid_trace.replace("|ex|", "|proof|", 1),
        valid_trace.replace(
            occurrence_two,
            occurrence_two + "OLP-0091|document-text|OLVIS-0091|3\n",
            1,
        ),
        "source_id|environment|finding_id|occurrence\n" + "\n".join(
            "|".join((unit, env, rule, "1"))
            for unit, env, rule, _relative in CURRENT_EXPECTED_DECLARATIONS
        ) + "\n",
    ):
        try:
            check_trace(invalid, CURRENT_EXPECTED_EVENTS)
        except AssertionError:
            pass
        else:
            raise AssertionError("invalid correction trace accepted")

    parser_probe = (
        "% \\OLSADeclareAfter{COMMENTED}{must-not-parse}\n"
        "  \\OLSADeclareAfter   {LIVE}   {body}\n"
    )
    assert command_arguments(parser_probe, r"\OLSADeclareAfter", 2) == [
        ("LIVE", "body")
    ]

    current_event_count = len(CURRENT_EXPECTED_EVENTS)
    current_rule_count = len(CURRENT_EXPECTED_DECLARATIONS)
    valid_log = "\n".join(
        f"OL-STANDALONE-SOURCE-CORRECTION|{unit}|{rule}|{occurrence}"
        for unit, _env, rule, occurrence in CURRENT_EXPECTED_EVENTS
    ) + (
        f"\nOL-STANDALONE-SOURCE-CORRECTION-COVERAGE|"
        f"{current_rule_count}|{current_rule_count}\n"
    )
    check_log(valid_log, CURRENT_EXPECTED_EVENTS, current_rule_count)
    valid_coverage = f"COVERAGE|{current_rule_count}|{current_rule_count}"
    for invalid_log in (
        "\n".join(reversed(valid_log.splitlines())) + "\n",
        valid_log.replace(valid_coverage, valid_coverage + "0"),
        valid_log + (
            f"OL-STANDALONE-SOURCE-CORRECTION-COVERAGE|"
            f"{current_rule_count}|{current_rule_count}\n"
        ),
    ):
        try:
            check_log(invalid_log, CURRENT_EXPECTED_EVENTS, current_rule_count)
        except AssertionError:
            pass
        else:
            raise AssertionError("invalid correction log accepted")

    native = json.loads(NATIVE_QA.read_text(encoding="utf-8"))
    trace_file = resolve_artifact(args.trace_file)
    trace_log = resolve_artifact(args.trace_log)
    assert trace_file == resolve_artifact(Path(native["trace"]["path"]))
    assert trace_log == resolve_artifact(Path(native["artifacts"]["log"]["path"]))
    assert sha(trace_file) == native["trace"]["sha256"]
    assert sha(trace_log) == native["artifacts"]["log"]["sha256"]
    trace_rows = check_trace(
        trace_file.read_text(encoding="utf-8"), HISTORICAL_EXPECTED_EVENTS
    )
    log_hits = check_log(
        trace_log.read_text(encoding="utf-8", errors="replace"),
        HISTORICAL_EXPECTED_EVENTS,
        len(EXPECTED_DECLARATIONS),
    )
    runtime_evidence = {
        "status": "HISTORICAL_15_EVENT_TRACE_PRESERVED_NEXT_GUARDED_BUILD_REQUIRED",
        "historical_sidecar": str(trace_file),
        "historical_sidecar_sha256": sha(trace_file),
        "historical_events": len(trace_rows),
        "historical_log": str(trace_log),
        "historical_log_sha256": sha(trace_log),
        "historical_log_events": len(log_hits),
        "bound_to_accepted_native_qa": NATIVE_QA.relative_to(ROOT).as_posix(),
        "next_guarded_build_expected_rules": current_rule_count,
        "next_guarded_build_expected_events": current_event_count,
        "next_guarded_build_expected_coverage": f"{current_rule_count}|{current_rule_count}",
        "next_guarded_build_expected_ordered_sidecar_rows": [
            "|".join(event) for event in CURRENT_EXPECTED_EVENTS
        ],
        "new_events_pending_native_trace": [
            {"source_id": unit, "environment": environment, "finding_id": rule,
             "occurrence": int(occurrence)}
            for unit, environment, rule, occurrence in CURRENT_EXPECTED_EVENTS
            if (unit, environment, rule, occurrence) not in set(HISTORICAL_EXPECTED_EVENTS)
        ],
    }

    evidence = {
        "schema": "farsi-standalone-combined-source-corrections-static-qa/6",
        "status": f"PASS_STATIC_SOURCE_BINDING_NEXT_GUARDED_BUILD_REQUIRED_FOR_{current_event_count}_EVENT_RUNTIME_TRACE",
        "audit_ids": AUDIT_IDS,
        "document_text_repair_families": DOCUMENT_TEXT_REPAIR_FAMILIES,
        "semantic_findings": CURRENT_FINDINGS,
        "audit": audit_evidence, "retracted_false_positive": "OLSIZ-011",
        "frozen_baseline": {"files_rehashed": len(manifest["files"]), "drift": drift,
                            "manifest_sha256": STAGING_SHA256},
        "fixture": fixture_evidence, "activation_topology": activation_evidence,
        "derived_source_inputs": derived_source_evidence,
        "olvis_0273_materialization_repair": olvis_0273_repair_evidence,
        "document_text_selector_limits": [
            document_selector_evidence[unit] for unit in sorted(document_selector_evidence)
        ],
        "corrections": results + document_text_results,
        "historical_environment_correction_events": len(EXPECTED_DECLARATIONS),
        "document_text_correction_events": len(DOCUMENT_TEXT_EXPECTED_DECLARATIONS),
        "missing_escape_correction_events": len(EMPH_EXPECTED_DECLARATIONS),
        "visual_reflow_correction_events": len(LAYOUT_EXPECTED_DECLARATIONS),
        "physical_correction_events_expected": len(CURRENT_EXPECTED_DECLARATIONS),
        "semantic_findings_expected": len(CURRENT_FINDINGS),
        "physical_to_semantic_mapping_counts": dict(sorted(mapped_semantic_counts.items())),
        "setup_registrations": [unit for unit, _body in setup_rows],
        "deferred_rule_executes_last": True,
        "corrected_units": sorted(set(source_files) | set(document_text_source_files)),
        "adjacent_note_units": expected_note_units,
        "external_upstream_report_submitted": False, "runtime_trace": runtime_evidence,
        "files": [
            {"path": path.relative_to(ROOT).as_posix(), "bytes": path.stat().st_size,
             "sha256": sha(path)}
            for path in (
                OVERLAY, ERRATA, BODY, RUNTIME, TYPOGRAPHY, DRIVER, FIXTURE,
                DERIVED_GENERATOR, DERIVED_MANIFEST, Path(__file__),
            )
        ],
        "negative_tests": [
            "missing_trace_event_rejected", "duplicate_trace_event_rejected",
            "wrong_occurrence_rejected", "wrong_source_id_rejected",
            "wrong_environment_rejected", "wrong_trace_order_rejected",
            "commented_command_rejected", "legal_command_whitespace_accepted",
            "wrong_log_order_rejected", "coverage_prefix_collision_rejected",
            "duplicate_coverage_marker_rejected",
        ],
        "limitations": [
            "The source-body matcher deliberately ignores whitespace, matching the TeX runtime; exact source-file and overlay-argument bytes are pinned separately.",
            f"The {len(DOCUMENT_TEXT_EXPECTED_DECLARATIONS)} document-text substitutions are statically source-bound but require the next guarded native build to generate and validate their {current_event_count}-event combined trace.",
            f"The {len(target_document_units)} hash-bound derived physical inputs preserve native TeX file tokenization and contain exactly one terminal document marker; none activates typography's active-dollar reader.",
            "Corrected pages require full-page visual and extraction review.",
            "This bounded audit does not certify the whole Farsi translation linguistically.",
        ],
    }
    if args.write_evidence:
        target = ROOT / "evidence/SOURCE_CORRECTIONS_STATIC_QA.json"
        target.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
