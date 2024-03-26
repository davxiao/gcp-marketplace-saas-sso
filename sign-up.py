##############################################################
#
#
# An implementation of GCP marketplace SaaS sign-up flow
# https://cloud.google.com/marketplace/docs/partners/integrated-saas/frontend-integration
#
# David Xiao <daxiao@google.com>
# March 2024
# All Rights Reserved
#
#
##############################################################


#
#
# this code is intended to run in a GCP Cloud Function
# it can be modified for a standalone Python environment as needed
#
#

import functions_framework # Cloud Function needs this
import jwt
import urllib
import json
from cryptography.x509 import load_pem_x509_certificate


@functions_framework.http
def hello_http(request):
	"""HTTP Cloud Function.
	Args:
			request (flask.Request): The request object.
			<https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
	Returns:
			The response text, or any set of values that can be turned into a
			Response object using `make_response`
			<https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
	"""

	request_method = request.method

	# per GCP documentation the cert url is "pinned"
	cert_url = 'https://www.googleapis.com/robot/v1/metadata/x509/cloud-commerce-partner@system.gserviceaccount.com'

	try:
		request_token = request.form.get('x-gcp-marketplace-token', default='')
		jwt_header = jwt.get_unverified_header(request_token)
		jwt_kid = jwt_header['kid']
		with urllib.request.urlopen(cert_url) as r:
			response = r.read()
			cert_str = json.loads(response)[jwt_kid]
			cert_obj = load_pem_x509_certificate(bytes(cert_str,'utf-8'))
			public_key = cert_obj.public_key()

		#jwt_claim = jwt.decode(request_token, public_key, algorithms=['RS256'], options={"verify_exp": False,"verify_aud": False})
		jwt_claim = jwt.decode(request_token, public_key, algorithms=['RS256'], options={"verify_aud": False})

	except:
		return '<h1>Something went wrong</h1><h3>Headers</h3><pre>{}</pre><h3>Body</h3><pre>{}</pre>'.format(request.headers, request.form)
		pass

	###
	### Add code here to take the user through the sign up flow.
  ### The end goal is to establish the link between the JWT claim's <sub> value and the new user account in your SaaS system
	###
	return '<h1>Success</h1><h3>Decoded JWT</h3><pre>{}</pre><h3>Headers</h3><pre>{}</pre><h3>Decoded JWT</h3><pre>{}</pre>'.format(idinfo,request.headers,jwt_claim)
