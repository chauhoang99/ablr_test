from unittest import mock

from django.test import Client
from django.test import TestCase
from django.urls import reverse


class TestView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_view(self):
        res = self.client.get(reverse('homepage'))
        assert res.status_code == 200

    def test_myinfo_auth_view(self):
        res = self.client.get(reverse('auth'))
        assert res.status_code == 302

    @mock.patch('myinfo_integration.myinfo.client.MyInfoClient.get_person')
    @mock.patch('myinfo_integration.views.get_decoded_access_token')
    @mock.patch('myinfo_integration.myinfo.client.MyInfoClient.get_access_token')
    def test_callback_view(self, mock_get_access_token, mock_get_decoded_access_token=None, mock_get_person=None):
        mock_get_access_token.return_value = {
            'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Il9SQzZ4d09NdmJ0dDZhald1WmU2R2xncy1qM3dtNXJpQX'
                            'lDVW9SYXNhLUkifQ.eyJzdWIiOiJ3MDI3NDlkYTEtMTBzZi0xOWZnLWEwMTEtb2cwMmp0cDJoZzEyIiwianRpIjoiW'
                            'XZzTEJSVkNLUk84OGx4b1o4bHNOUkdDU2paRzJCRGN6OFFONjl6UiIsInNjb3BlIjpbInVpbmZpbiIsIm5hbWUiLCJ'
                            'zZXgiLCJyYWNlIiwibmF0aW9uYWxpdHkiLCJkb2IiLCJlbWFpbCIsIm1vYmlsZW5vIiwicmVnYWRkIiwiaG91c2luZ'
                            '3R5cGUiLCJoZGJ0eXBlIiwibWFyaXRhbCIsImVkdWxldmVsIiwib3duZXJwcml2YXRlIiwiY3BmY29udHJpYnV0aW9'
                            'ucyIsImNwZmJhbGFuY2VzIiwiYmlydGhjb3VudHJ5IiwicmVzaWRlbnRpYWxzdGF0dXMiLCJhbGlhc25hbWUiLCJtY'
                            'XJyaWVkbmFtZSIsInBhc3N0eXBlIiwiZW1wbG95bWVudHNlY3RvciIsIm5vYWhpc3RvcnkiXSwidG9rZW5OYW1lIjo'
                            'iYWNjZXNzX3Rva2VuIiwidG9rZW5fdHlwZSI6IkJlYXJlciIsImdyYW50X3R5cGUiOiJhdXRob3JpemF0aW9uX2NvZ'
                            'GUiLCJleHBpcmVzX2luIjoxODAwLCJhdWQiOiJTVEcyLU1ZSU5GTy1TRUxGLVRFU1QiLCJyZWFsbSI6Im15aW5mby1'
                            'jb20iLCJpc3MiOiJodHRwczovL3Rlc3QuYXBpLm15aW5mby5nb3Yuc2cvc2VydmljZWF1dGgvbXlpbmZvLWNvbSIsI'
                            'mlhdCI6MTY0NDU3NzkwNCwibmJmIjoxNjQ0NTc3OTA0LCJleHAiOjE2NDQ1Nzk3MDR9.FZ-Pl2G5LEKoC3sQHUPYBy'
                            'XLi-jqSS4B51pp19p-jKdPUZQFukLJHVXAPTmufGSPiBOD0OwwReowoKvLvHD5E7FqqNFeYdEQsD6QfTHVu9TB4gwE'
                            'omppdd3na_CoHrHg-8hTzHsKakc4O0G4SFrQY5z2pZiLDv5TzZi5i2uH92izrI5G9KfupARSZerF5oIEuW6yCMgaRO'
                            '3ttupN0NEe2IpuByDb3rNrGIcEuN3GHks5EpOFzEB1xH7e5QMnzCa5-2cNaGwhrQhf3lyFOWmI0MDLL5TzHiTyUr2e'
                            'cFcNoXHRq3Kvedil5KYYxBU4AbT4FhDC6FKp4ZsHEfFwXQrLcA',
            'token_type': 'Bearer',
            'expires_in': 1799,
            'refresh_token': 'FPoSGxjIxOp7w8MWCoQNt4jc0syo3oqN8-9S5pMG',
            'scope': 'uinfin name sex race nationality dob email mobileno regadd housingtype hdbtype marital edulevel '
                     'ownerprivate cpfcontributions cpfbalances birthcountry residentialstatus aliasname marriedname '
                     'passtype employmentsector noahistory'
        }
        mock_get_decoded_access_token.return_value = {
            'sub': 'w02749da1-10sf-19fg-a011-og02jtp2hg12',
            'jti': 'YvsLBRVCKRO88lxoZ8lsNRGCSjZG2BDcz8QN69zR',
            'scope': [
                'uinfin', 'name', 'sex', 'race', 'nationality', 'dob', 'email', 'mobileno', 'regadd', 'housingtype',
                'hdbtype', 'marital', 'edulevel', 'ownerprivate', 'cpfcontributions', 'cpfbalances', 'birthcountry',
                'residentialstatus', 'aliasname', 'marriedname', 'passtype', 'employmentsector', 'noahistory'
            ],
            'tokenName': 'access_token',
            'token_type': 'Bearer',
            'grant_type': 'authorization_code',
            'expires_in': 1800,
            'aud': 'STG2-MYINFO-SELF-TEST',
            'realm': 'myinfo-com',
            'iss': 'https://test.api.myinfo.gov.sg/serviceauth/myinfo-com',
            'iat': 1644577904,
            'nbf': 1644577904,
            'exp': 1644579704
        }
        mock_get_person.return_value = 'eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00iLCJraWQiOiJzdGctbXlpbmZvIn0.jYlTF' \
                                       'rqAuEXAEKvql9TyyRuSIwide_iEmaStBbqG9GR47YCef4Pd9k6snyYCZIVYlFztP6hw_TZSsh7ics' \
                                       'SCtf5m-NOLOZA2L_WL0wNVENtUwZpASZ4a7hzQFykp0nLXLZwvns_MbA_mJXKkQillz7TmnOHPDGT' \
                                       'p3U2fEZvIaVB-ySkvIaOHJmRLZ9QgKYByAourAmitBjoZZetg4vzNtuQV2rGdJT6cB4U5spimEn2K' \
                                       '3631mVulk-p5_eicTu2k3ZVWR9u6P6gOfD2JRGGUC2XlT_qWac9JwLBwgV2icAqKrLpFWa_nWWbP1' \
                                       'quk-FGCEtGmOKFNeBRM00S9VhWIBw.Z8dYubMmnzmSfGx-.MhBcoXBT9CkpViStgc5yl8LrN2o-Hs' \
                                       'KwPtdHQtx1CSXlZ9AxlfecQMIAHm43ZorLOEq06775xu5oWm7a2lRV2UhoqTvtUKkhJVrGk4BwTrj' \
                                       'Dkif0QPhSNtc9ANBJp4t4-lY4cvCtcUbMAzUVz8wDkvpoivO6-4nYs4Sb0xB392fmrnuQXrVPZoGR' \
                                       'NnFMnu_f6TwrC24gDRL4AEisqVx-N0-P-CBx2g-xRM4bo7vapKfnIU9khx4-qNj4FQXD44aNG0iMZ' \
                                       '4Z9S3Hfws57qPrvu_sBxvMJhfB6_taHWc1Sx1m1LaFa5o7OKJ6O7SqvWhRuEmieAT0scrg5dJzddP' \
                                       'gGOePsUSlo9IIQZiZZvvcK-DtTpsAwjqK4-JxqWhnaAAmuUBZPFuR4xZZucQheMZb_VFfcWh_uh0N' \
                                       'QUgGE7oEuBxlaisF9nT-9AD6BBA8D-KeHwsTyb6UoEjpL2i0ELYsDbMM0CTU2z6_nioJW8tR7d2rr' \
                                       'oDRyHL4QbPZSKl9_PmgcURmV7aDnAGBcjuvQw21buV2sYgzKR8M8UWdTBoTPMwPl96oyWFAeIRRnR' \
                                       '8Bynx0OUyup8DGBZmIQcDSyDS7yF-WvVKEvODTIxmFEmqU_7M1SENoPjjE1hlj5hC2m5trnbnK-1R' \
                                       'njJj0uhGR2diIXYfmeDLaxVwlERzNByfYbkLMzQoHALz8pzQh6wPYbhg6QOYQ9TCWVL05yskVBiP6' \
                                       '9hhbLEGRg4TWCbcGa1X-T9ewem506Jy3LvglgHxQXdeJImwa55GhdjqsABDwBZbS4dfqZ_VmK4I1M' \
                                       'WMcOPwB9bJURo_VGO5R2JoaIn7rfB4tN3DwsRY_lolGka8Vu79RqzDzH1PNvCIK1ubbHgUjHbemt8' \
                                       'wvRTBZ8QjL6DThL2YqtZHiawlEjAq_6e3wqxZzeH3xIoDdwGE63i5GLuZSxdupm0OHBvZgwB0rh_k' \
                                       'VKI7_eSzemNe5yZmrfHJHlwTCp2s9zMRhsxMhsREW6lrICAg_J-MfvQTXSBdcXJ2ej95IODzgYVSg' \
                                       'O3Re26xqQSyZ475G27xn-uBVFzodj3HVk_65s-ZIRLcoWLgwHuKQimpL7swbCJ3ecmDcI6FwwWrbg' \
                                       'K7I2f-42Tah1bXxXDVGFz2myS2anIZ4bkda-Q_q8Qczn0JJNL7c9NguZ_hQYQyX-bdXD8uBhNiGkq' \
                                       'yJmFHrFJjanbw2QJjUUfEHcr3SF2jrMvUdDDar5PhRVTMFiu6TBkFr-tzdoq6SKxpMc_DhbToixST' \
                                       'O6HbT9wReiqQotPU6Ka2AcsCa3uhvM_Q_Y_o20jGvikgerYxognpr74uBQ5sqbKha8ydBzxopFDXz' \
                                       'arGOb5TjLcTkkvy2xZtRPZQ8prmY5UWcIkA2IaLF6n1rHft4gu7GzhoEvCCnsN4fCoZGlwiGJ_ks0' \
                                       'Vtv_mBV1DAHs9_V7LC7DJH9SsOjjBnkb4JRhsLl_2hrhASeyabzs6W9PR23it57bX6WG3gcbACvqr' \
                                       'lhTAw0NlQ9xwjZpxEzf4zZY4eiZoDdseb7Tv6JfRg1ljUYj3D-08ZfhLJbpEcvoGLMruQm_u8ru-G' \
                                       'zD1XfhXUDsQ3UtcmG-m7lw9ANaMJJz6tG06-x5M0T0Xz0Z7DmzBOEmooUDjkyOcvMVK2tzZBSQmV7' \
                                       'YXy2KfRbd0jF_SsuUR0ktXIZbBXdxGbrvtJl-7356Fo7tnHy9ygE77ZursYrRSXRJvv_ZOIi06Eyw' \
                                       'dhnpiD6MMjnARh_OtIqqi6Z2nX23LsgssyY7Mc2nFQRFAi5XxtOO_XdkUN19mdLQ7rSxPhEYbWM0m' \
                                       'VCaANKEpWe9z6p2LJ9cTFZXTrJRLHJ8gOfutGUj3YqozNezj1bqxwTbdyQJ4AU6nLAkhKbJJLJ0CG' \
                                       'BhWD05ol3JybvcY-Y-B_ZxrSxHOpMrUgI0WDMD6xM8tIu-rbCXKDnAskABQRbZnnOW-AxGLDQWPJX' \
                                       'xM7C0QbtHSkUcJBHOOQOK6dBvM1fRMyK2NP6H5LxKgHrzkM3_RSA_IbO6_zawW0NBfEP-a2AWvSPz' \
                                       '60YZwAXAPqFiLOOJQiQ4fzgBebwGwVfCM_0AubzJJUX3HmxHqd4155A8aS8Yg7f9e8PWA5cJKv1Dy' \
                                       'td3q2Wh801Pov0EiZPoa40EfOeJuBOTXuhxAx-ICdCYhnGh_fx5h6rIf-qrNVUEduZcI6dvMQfTWq' \
                                       'l3iu2_hdNUUR2E4BoPJFTeX-eoRWBaYuNmdz5uifm5L4pU_R0etFS9HCZcB94hzN3jiwu-VUTBd5E' \
                                       'dPWy6wtxH2Th2r7Hi7mX_CDStLqoK9bAprV5faMduijrrTQJUWYZg-zQzuT6ipnkFauFwaKA1BvJQ' \
                                       'SM0KXfxQdoJ9Q-COZy5q6dTU6_9NMY7zUTAtVpyYlpvIrbTXJAdFo7X8tRO60JMrf3ZWRJZVXdEmU' \
                                       'H4iyKO2YY8t4YItCWM50o3oTCBwn3YCRyusKa1vB5qt4hmhDzUg48ygWe2K3uWAVLyMwZvoWAVMUn' \
                                       'AJ-ysPt_JFNRD8FEYUweOoBpFh_A_DPQfqrELxHVgy-dincr7_numgaTJzUQorchbaFf0U6jkhJ0m' \
                                       'QI7CGxrG27wyiZuu382GVZkWPx88ZhPE-x0DByMRXARX4e-EtNUOzljlqXTYRe9UrHO1IDwscjoM0' \
                                       'pwYqa3BfMMN4HBbWCtsk4bSj6YjArrGjjKfnSdAnxIcW5QxIZeVTd3oB92gFoZATMf31It5CEZtJp' \
                                       'h8GlwGlj18C_ieWqvf69IXWy-DsHQJU6VaCLpdaEpjjmTMxdgr_u_5XID7sqi_Zv1yuaZBG-5lr_V' \
                                       'XUvhD1tJnE-xRfJ2Mq3r87mm7IUCBNeXbE4jCjAs4ROx2eDyyUs3HSTCTtQP84NDeqb6AEbra4m4l' \
                                       'veKp3mpheCgDcd1ffIk0JkOk0Ulq9t-9ZC_DWqsb1dvemX7W_78z6D4f27knT4b1OJdL2ujIsF-UF' \
                                       'jgE_RQ0L9W5S0kSNHjj66GenJBIPQ1-GSfa3kDJqv4bTGRHAkzhpO04hQsJnTiZzJ6S3BQqvgFDWI' \
                                       'BhJj5n3EAgpmmIlzwE1NTgrta6cVFYYLUne3SZr1d7HiIm6isGY0akXXOYV294qkzFkSs-e92_NVb' \
                                       'DBCwghFZgII3m85JbAMvhBjYID_XGJtbzaI1O1Xox6rL2LQNFqcPnplPd2OX6yxwUnhyaJ6FylQ5W' \
                                       'YksACuLM6DlMwObpN6QlTFonEETauPQVrtklPqugWUViTLEr4HoTJHTQWPIAIiS9Xl_EloXBlmLbo' \
                                       '3swYYxDP1WZDRQmUsauK5O8aOGLKgTzXkKvjQvrX8y-EgqyAuNR_8FQeUxBqVjRofaXgPeCQlGCL_' \
                                       'YTaCEM8B5xwuNtts4SfWZ-Q3PDGlYFOFui8n19VmjsIe4IB_9fn6vbcggjwWX65jjdcI0D7RX_sJe' \
                                       'TVy18UfJwuWcYZmSXl5JOJm_qMA7RjKovvv2IHgiZJ_Kx7RZ9TxviY94FLqQ6y-nbSe07Msx_n28k' \
                                       'Utw6BVH7FYmHw_0bZkwk5lbBeml1Wfl0-HxZSgBIdzqQiCVdrWnq65Cx8B74QJjIL7iK3EPMGL0Ei' \
                                       'FY6_C0TrIMirUj0snHGJPP4KWPa6EMmnY2DUtrVjrxylC_mdQRMnhmCuaAaDFosc3lq43NbRPyeHW' \
                                       'h_ne94xRESpmrOL1X9zJEeQIh1sVjFMG6uEk3Efx4EhKc7zizO5PG9K3-5GL9rx3s2hw9f3pwVkCa' \
                                       'DTVetqEhS5VoWJkHe1vORbpXypmRQzEswGkQyQer6KnxRBW4vKHDfJ6glJJkWujrclPptoYbRzI6X' \
                                       'Y6yHIxVPWsggN_MX3oK_A24Tvje0m0BGmyTeegK7B9pq50jUms2yFDs3d-jvPHSMn8kowd_1aVPK4' \
                                       'yGnl9dSiOCUhbiGEtBU29zFROtBbX9Ygog48iTZw_du0yOWdAK6BfUXbbKGFWL16j73MMDxEBtgGI' \
                                       'i7YEPecK9UWtJx8tYe7CmK5EJaNG26sX7eAYDHNc7MYCzq6cf9yivvJ4JKfKWQb8EkWxXaflpag1v' \
                                       'TpSQ9farQJO64xApW55tnZzio_L_mLgRwHK1m-EMAZBRxmIWhVYdi7cIylCGUSHNG5d75hozQ8rrb' \
                                       'QatLGyKF-w3otTu0YpiZubAsFiA8c6Qu9AHP9Chp0ob86X1qxblCaL4u6aZ5lLoWaz5no-Ko38qvN' \
                                       '2qwzgWkkpmN33HpJCyOHkbq5Xsz_-H4zjieFKcJ9tjtOVKgRXT1MCAOVA-3UZ9VM0Ubi0M6oFEy7D' \
                                       'un9ValbSSRi5V9n98oENtSvUqyaB0upouccOWCDEPhZKN0fnhy_vUwWzKxSm_rT9bEssOPH1zZv0M' \
                                       'GaDNazjPbDRydBveNp4Ybd5qn63_Ms6rjFjrK12fRmgrZNEKEt7bKyOrPmFYHap4H-VKIO3vuKoWb' \
                                       'xeUNbdtMVngloey-6pzp2X4XobANxP74qUf6OpqWgVJkVDObE9OYrXPCd8H3lG6dc7Wvg-31Er1p6' \
                                       'YT-VwEHlo0Spo7ZXaA-yDUbT3XnE50cnFyk2XSrEc86FxKE0KiAPhfsDDmn37JWtnwjAQbfjeuulo' \
                                       'QNBiHFxp72Yii_44vxV1snq7CsxqRPGBT98B7mVF8T8kfqO_au03FYpNAZOHFfXsmlFmeQSWmVE_2' \
                                       'BuoXB2pPKdMfNhLIsAnWWCcCYfiJ_l__BtNE0jesfjuFGtGaG7230DBcKC5GRZKMSowJK_Zei0-h_' \
                                       'BqMsFX_Nd6ZjU4-MnwdJHdZeYX9ckmA7neXX-c_PodQafXPC-eEBQFj-hTmrS9x86uOsyUf0Ev25R' \
                                       'G6CoCf0FBZd9KWgn0zXJGGb9XvrgtQn--zOLHnxakIwmwIWXPkiRY182GFRsHToZpsRrRlnm03jkG' \
                                       '7vOIr3_V8s9EtlLPeBNBoipB1dpKSnhX1sysBovDbw9ApsNXcU-xqUd7GjXz-p_8CEhbcgZm6ZO6C' \
                                       'S4Wp8OXUXdP5OnOrudD1KrEvnJ7NCsZUaFVvV7r6fI9og7a3BhcdCqy8OtrGDmPTiy5EsrcapniBg' \
                                       'YPyO6JEGiJ0ebFv2X-lLMZ-DQWPXTCvS6qQtzQNXAjWSTIPYEfAs8Hg345aoZqjLf80CkTHlYIAZC' \
                                       'R8AuLNBoPEUUb1A99rk6GkACzwGmNYReLPXjuXGh3vZVacGXh1RUmEdE8G_FIZBC8j2mTari_9Vap' \
                                       'CXcD1pluj6jXmDuEeP0P8SPqPuo3VYKnS6_9DeZGtbyTchvc_wMzh4kH6BQoSseKC53pqoDnljoel' \
                                       'a4eU7rYfvdoA5Hkl1iVk2r4Crdv6zx3AUqRq7Qo8ZXhnk7-u-9PMH5IW4wDHmV3GIpjc9i9YccId4' \
                                       'bt1O0vJDZAM4mDtm2ezejLLc2bSlZPLi7wMuJ1bsKMmvTm5N2K4dALcNUS0nDT8tRxwEUtTwfjhhj' \
                                       'T_rrllBv8UjH6ERE9O39Pnb8dnwljOcRTdGOkm3eSdETOb4FwlkU2w3-VoYGFINq-cvghxx-NBeDo' \
                                       'gLWbiwXySYnaHQ6ab_qx1uvkKpERB-T6ufBybD5szT_Fa7qy_0yVrAMthnPtv-SawM2ZMCGmMpnMK' \
                                       'KfDH5M_cl3n31yTqB97ozGqvxpuYY08sMxi19noxth9cKM_GFbPL3Ir64GwFDDfZfqXhoOmXSO3sg' \
                                       '3WcVeNygoikuuxbbUqlRMqZBZdwmF1XUUI1rfzLjB8yvauy0DbF2LgOI6OyFa04YZGDXHcQXW8CAW' \
                                       'VKHkJDuHLgoS6hD_ZySh1CtiuDvW0Lr2a2vVhPOMlx7yAbBrEr3Mgy0-aHVQ5pdKxTCo6OQki0Tzg' \
                                       'OPQ3XENJSC8vmtt05lL_qiYEuYN0rlBzhxdYz-j34qB3WeCS-55jCvldlUbDqmB4jBeD-KMeSxf9u' \
                                       '4JX1QqsdQGBiVx7zpKir9TmfNwxnEcuz_NKiPKTkKiK-XIWepUnK1lMeo-4Busc8jvSG58w0O7ixt' \
                                       'qRdqKd_V5VGD-Pt7S1iBz1lfjwMRr4rx4VnRiReaPrzrpOTnUoFCaBfabzx_xgDvpj1LxsToNvl_2' \
                                       '75J0h-aojprmjqQes23GaInFZWrhwn4gxbpvpEscxAi5GpLi3_X_7vQ5LACqjL0dy9-DR9uGRjywV' \
                                       'zCRSv9BakUYhxkoqtPIqFF9N9NJ74KdV7HXqJBZSDOUwDDElajsBFxA3lhFizJWD0hox8Gj3p0wV_' \
                                       '-Vf1rsRKXWjWYMgSdc8V4DZHl0khf_NJOIDdLDWJFBgqAPcuVrwnsA-MdECT-3d1pQ1-K0rzF_2sa' \
                                       '7dKBfIZ3B3yomul3puTVt8QDZ3zFxMMYKsvlK-OVnH__4sNa9B6LCaAmpK_llaq1iVnOo860xRAQc' \
                                       'PycokHl7mDomEpdZJaqAiK8S3QN4_p5k9E8-BOf_ZoD3J6-TOlwuVD_0M3MqTVpd91ntyspPnACro' \
                                       '2CIz5dbVyTG57ClgQdTKpnGiHFhc5hfMzjxSp3ON16LZuSLlxiwkqg1p7QnDaQeEaaeBbwsJMkWOr' \
                                       '9S_HOGavtk5Ilhyf7H3XFO9bELBqrrM2uMmZ7nphTMDP-ogk4nuuMEY3PPMYN_44Mf6-J58tWc0aQ' \
                                       'ZzWBMfe8NyBB6-WC0IL6Z_MruS6rG4OffDYhh1wiwfgmAWYEbzvq--lYts0HeylLjHoOBi4e5s1bV' \
                                       'CSZe22HB96hbrI_E3o2dG2MZUrLRl3LtFF1fIx1Hu5i8Zr7MYNKA6dx4HayJCK-VsRvldAhDppFYM' \
                                       'wk1aOQ4R6tt-1fgReEHDhqZqnTVVGwQmWpRcahcl5qRJpzog4WjdsJv7t9CWzoNh3CYjBBYpSCSx4' \
                                       'sg9fO1AR7K4HLitsSk3KjIXfPD1aVAlVyB_a5r-si9FPkeLfoTImgqL6RoWMZbG4wW5flPPhqwkxP' \
                                       'Fih9b7339taBsKV-vt89wdIT8ulQqSO5fgLRkfJt4R_EIL_piW13KH6nZlCUy7yZxp1c6qXqwOZRN' \
                                       'd1cczT1-LBTrtaTP1QWNJSqrIUGP42og9St7Lcus-BogsAgH6isXEYWnas2v3rjJSngFymrA74TiE' \
                                       'CRm96Mgu8SOg9KuEiP0VUMPd0-W62I2JimQBsLcJz8EwVSoYBanBN9ozx6sccg60DrGUuYzKNixYd' \
                                       'LhRbOCwK_YqIUUUajBwqWxrcip-dH3kdkthG1JbkAMIkFLEDjhgl4HsxobG2Cah7GANgs999-RRJE' \
                                       'lOyFyLGNAOA278QTw3Y6QE4y0MIyb24Ksy68vQrzhlGcN_RFPJr3yLEzSsBxKx5fFLdY20gHfn_-E' \
                                       'TXTJBZnOctmt-y4dqxkyG4mX6S09-0brL4alYsSJA5Swlsojb2s1FLdImwY_Wj3HErEG8GWK4ySQY' \
                                       'EfTdFGH3VSGL65TtHcTa1vuO_AbVomOQTjdv_0GHh-U2D3XuDF_FIVrIhGSpyBhURBR2BSpXH092q' \
                                       'Q_Et5D7gJ7A8BX1U4K2QVcbudUlD5-4GTsjg4E4BR8yZL38fpa1ZHXZgQvp2kahJOah2nwWkAs7_e' \
                                       'x6liL3WdbiiKsEwLqH32dTXWUhN-5T-ll_iySNnY-sgX0Hprnz_bd4xGZGr8F4nzZJi1FSv6PiQ7q' \
                                       'ABwlnKoAZ3ZN7Dquljqx_UIRv7dWU8Pq-5ahCOewy4UBeEwx-aFr7ooXBxyPXdb5sncZvTHc9Lqi8' \
                                       'cudjtBh9JMoJ7d_rJXvOA2pZeEQt9ex6mDKbMQbf5f7fw-Fp3AJdvP7hUSJM_lC2KKPRHxJgKTTof' \
                                       'V6aM-lQxVNE2_hw1JrftXrmyenCUs8I5Cxy2_dwzI77ThIIBLIx4HGQ9Va5RBwn8o27JELsOSHKBl' \
                                       'Nv7sCzu_vankSJrqGMEQnrAAiJCj_IeH7ms6gGMsuXSei6CAY0uaoc_GsVAjTYb2dP0btP5i6enwC' \
                                       'QKutTVFaU1FVs1z3QgsoS-jkyMmuRbvlMIF9H8Yka90qN1kIkSjXBCLg2EtW7kInrSV0-etj28EDs' \
                                       'bsf3DBB7OJEw5dmbxf22xHYk48KiloE4iwo7Td7B6CCH9_34IJLIC3zeBZe_h2_NpQ4ze0TgrRbzp' \
                                       'XG71ActOFGmNOT4G8zgnnzeNKxaYSUucVsMFPsNpWCFaOuda8zV5y-LUbZJzc-mvMMh69nhnMk0Ij' \
                                       'jMcBiXDXiwTlBG0_dV0SKHTrfCLEErnlVz9wIPSVU_fayJWqaJhQ8YRg57mMrFI-JHyP13nD4RcWQ' \
                                       'k5ZHnHYQyNsPvimdWovnCuhdsXsRJUBpPtVDyN1mPC-1HFKr_wZyR6HsMC_l_FCjpDAzcfHA4_ARh' \
                                       'lHfacuJU-ojtZhievG9KSFxWBf2w8EYPgekdat7s4NIQ3s2M58osFpwFJKGBxh2zGiLo6D7XitU5r' \
                                       'lwgxCvrW4_1ziuKI91WiJvb_J9ICYuarsZ4nM2IpB_EMNhVugrbUNruH7mQdasPZWKla4ViV1Qt4w' \
                                       'LpVD2ARTVgHgpmews3X0cr6VBzu4A0huhkdlEJfFBfRwryHBXHURwZDuh1cDMZwxZJjc3Cx5LebER' \
                                       'nX0MPOVHTDC4jg-SZdyHm9o9rUVwHFXEeAQANvNMlOy-M5zrp0bl0AJTAotx8sn3IgzoNRBCv2c9C' \
                                       'xL8mHOeeRnS8JlTg5Xgr3nhzTjrUftLCX6hSX8ZjZtWqrUBLKlz3Ss-Ds6fvN_uGwKE_mEbJqRjhM' \
                                       '-hbklok7gqVYOvbkiga4TOiWgQft2ucdHg5u961HfgJqO9O9WrZerqoiosUH0RaG3XPZ6rqElinXG' \
                                       'WXwh03RrtrYgP5VNTtUdbjRyBfgWyJ239I4Ddc-d4aKbdnTem6l6QsouG49F6Y98igjzp_IO0nHow' \
                                       'U5lmGBTqlFhxGfyG8FsNNqpKztBbSpoJqGY-tkJdl_V5tdLQdNA8kCeDJzpoHNCnQ-tdwjonqgWDa' \
                                       'g2oK6YyY2AaLtZWLfMN8S0SV3Twlyg7Ou8HzV1kyvwgM602n2P9llz_dpj1BbJ7ZZt_qfGjXNORbo' \
                                       'N4GkMAtPUm7mTftsZaDC425PvgZbGgZpKr6kYY0q4YeGv7PNHlNwxgEcrcalJjG6uKsiVvIG-cJNf' \
                                       'KxezLdFh7dT3mY23yMnJvm1_62UJ1hq8XmglbgGlbB5VmFYnlvTqw9YTGa24GUSk6Ub2NJqMIuQzA' \
                                       '4T7_OQOw8tOI2xIsIJdGsWJZB1RX0L_uLiaR1jHNZ2p6OXP0XrbPMGSe9egEf4uNYwzSrI0UW_ToO' \
                                       'V4WIsxAfrlHYVe2894s3dx_iBpOLQbffJqwmimETPk8kBAeG0qPXpZ3dbdWtkUh2hnSP75BXR3fGF' \
                                       'tbq-5xeBGG6wH7Tpbg9uMH0kOzFde_0_Q1TMzrQoos5a314QEv49ndY5IPjxL62RRP6GDFqfB-f2g' \
                                       'JOuf77DdtjtdD1vWoHc_perRoA_NYbjRbgTRSOsd0eabzJ4GGxNa2e9nuL2QKv5D6vl41lbkFAuCi' \
                                       'qkcjJFeTxQG3LZs2L5sNQC3Ed9GgSyTDEir45l4NHDsM4EerghDbq_p5Sb_k9a0rVWgjcYXLOjFjX' \
                                       'fHm02ACFdsvMyKA_bguXXljKXHVvg.DhNs-_bxMF0GL18T2fjBVQ'
        res = self.client.get(reverse('callback') + '?code=testing')
        assert res.status_code == 200
