sample = '''<ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Thread Group %s" enabled="true">
        <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
        <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">
          <boolProp name="LoopController.continue_forever">false</boolProp>
          <stringProp name="LoopController.loops">1</stringProp>
        </elementProp>
        <stringProp name="ThreadGroup.num_threads">${users}</stringProp>
        <stringProp name="ThreadGroup.ramp_time">${rampUp}</stringProp>
        <longProp name="ThreadGroup.start_time">1302713373000</longProp>
        <longProp name="ThreadGroup.end_time">1302713373000</longProp>
        <boolProp name="ThreadGroup.scheduler">false</boolProp>
        <stringProp name="ThreadGroup.duration"></stringProp>
        <stringProp name="ThreadGroup.delay"></stringProp>
      </ThreadGroup>
      <hashTree>
        <LoopController guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">
          <boolProp name="LoopController.continue_forever">true</boolProp>
          <intProp name="LoopController.loops">-1</intProp>
        </LoopController>
        <hashTree>
          <HTTPSampler2 guiclass="HttpTestSampleGui2" testclass="HTTPSampler2" testname="Site Perm SharePoint Settings" enabled="true">
            <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
              <collectionProp name="Arguments.arguments">
                <elementProp name="url" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">${siteurlnum_%s}</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">url</stringProp>
                </elementProp>
              </collectionProp>
            </elementProp>
            <stringProp name="HTTPSampler.domain">${server}</stringProp>
            <stringProp name="HTTPSampler.port">3141</stringProp>
            <stringProp name="HTTPSampler.connect_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.response_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.protocol"></stringProp>
            <stringProp name="HTTPSampler.contentEncoding"></stringProp>
            <stringProp name="HTTPSampler.path">/reports/site/permissions</stringProp>
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
            <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
            <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
            <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
            <boolProp name="HTTPSampler.image_parser">true</boolProp>
            <boolProp name="HTTPSampler.monitor">false</boolProp>
            <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          </HTTPSampler2>
          <hashTree>
            <AuthManager guiclass="AuthPanel" testclass="AuthManager" testname="HTTP Authorization Manager" enabled="true">
              <collectionProp name="AuthManager.auth_list">
                <elementProp name="" elementType="Authorization">
                  <stringProp name="Authorization.url">${baseURL}</stringProp>
                  <stringProp name="Authorization.username">${user}</stringProp>
                  <stringProp name="Authorization.password">`1qwerty</stringProp>
                  <stringProp name="Authorization.domain">${domain}</stringProp>
                  <stringProp name="Authorization.realm"></stringProp>
                </elementProp>
              </collectionProp>
            </AuthManager>
            <hashTree/>
          </hashTree>
          <HTTPSampler2 guiclass="HttpTestSampleGui2" testclass="HTTPSampler2" testname="Site Perm First" enabled="true">
            <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
              <collectionProp name="Arguments.arguments">
                <elementProp name="url" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">${siteurlnum_%s}</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">url</stringProp>
                </elementProp>
                <elementProp name="loading" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">False</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">loading</stringProp>
                </elementProp>
              </collectionProp>
            </elementProp>
            <stringProp name="HTTPSampler.domain">${server}</stringProp>
            <stringProp name="HTTPSampler.port">3141</stringProp>
            <stringProp name="HTTPSampler.connect_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.response_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.protocol"></stringProp>
            <stringProp name="HTTPSampler.contentEncoding"></stringProp>
            <stringProp name="HTTPSampler.path">/site_permission_report</stringProp>
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
            <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
            <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
            <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
            <boolProp name="HTTPSampler.image_parser">true</boolProp>
            <boolProp name="HTTPSampler.monitor">false</boolProp>
            <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          </HTTPSampler2>
          <hashTree>
            <AuthManager guiclass="AuthPanel" testclass="AuthManager" testname="HTTP Authorization Manager" enabled="true">
              <collectionProp name="AuthManager.auth_list">
                <elementProp name="" elementType="Authorization">
                  <stringProp name="Authorization.url">${baseURL}</stringProp>
                  <stringProp name="Authorization.username">${user}</stringProp>
                  <stringProp name="Authorization.password">`1qwerty</stringProp>
                  <stringProp name="Authorization.domain">${domain}</stringProp>
                  <stringProp name="Authorization.realm"></stringProp>
                </elementProp>
              </collectionProp>
            </AuthManager>
            <hashTree/>
          </hashTree>
          <HTTPSampler2 guiclass="HttpTestSampleGui2" testclass="HTTPSampler2" testname="Site Perm State" enabled="true">
            <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
              <collectionProp name="Arguments.arguments">
                <elementProp name="url" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">${siteurlnum_%s}</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">url</stringProp>
                </elementProp>
                <elementProp name="loading" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">False</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">loading</stringProp>
                </elementProp>
                <elementProp name="with_subsites" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">true</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">with_subsites</stringProp>
                </elementProp>
              </collectionProp>
            </elementProp>
            <stringProp name="HTTPSampler.domain">${server}</stringProp>
            <stringProp name="HTTPSampler.port">3141</stringProp>
            <stringProp name="HTTPSampler.connect_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.response_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.protocol"></stringProp>
            <stringProp name="HTTPSampler.contentEncoding"></stringProp>
            <stringProp name="HTTPSampler.path">/site_permission/state/</stringProp>
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
            <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
            <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
            <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
            <boolProp name="HTTPSampler.image_parser">true</boolProp>
            <boolProp name="HTTPSampler.monitor">false</boolProp>
            <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          </HTTPSampler2>
          <hashTree>
            <AuthManager guiclass="AuthPanel" testclass="AuthManager" testname="HTTP Authorization Manager" enabled="true">
              <collectionProp name="AuthManager.auth_list">
                <elementProp name="" elementType="Authorization">
                  <stringProp name="Authorization.url">${baseURL}</stringProp>
                  <stringProp name="Authorization.username">${user}</stringProp>
                  <stringProp name="Authorization.password">`1qwerty</stringProp>
                  <stringProp name="Authorization.domain">${domain}</stringProp>
                  <stringProp name="Authorization.realm"></stringProp>
                </elementProp>
              </collectionProp>
            </AuthManager>
            <hashTree/>
          </hashTree>
          <HTTPSampler2 guiclass="HttpTestSampleGui2" testclass="HTTPSampler2" testname="Site Perm Second" enabled="true">
            <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
              <collectionProp name="Arguments.arguments">
                <elementProp name="url" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">${siteurlnum_%s}</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">url</stringProp>
                </elementProp>
                <elementProp name="loading" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">False</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">loading</stringProp>
                </elementProp>
              </collectionProp>
            </elementProp>
            <stringProp name="HTTPSampler.domain">${server}</stringProp>
            <stringProp name="HTTPSampler.port">3141</stringProp>
            <stringProp name="HTTPSampler.connect_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.response_timeout">${socketTimeout}</stringProp>
            <stringProp name="HTTPSampler.protocol"></stringProp>
            <stringProp name="HTTPSampler.contentEncoding"></stringProp>
            <stringProp name="HTTPSampler.path">/site_permission_report</stringProp>
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
            <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
            <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
            <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
            <boolProp name="HTTPSampler.image_parser">true</boolProp>
            <boolProp name="HTTPSampler.monitor">false</boolProp>
            <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          </HTTPSampler2>
          <hashTree>
            <AuthManager guiclass="AuthPanel" testclass="AuthManager" testname="HTTP Authorization Manager" enabled="true">
              <collectionProp name="AuthManager.auth_list">
                <elementProp name="" elementType="Authorization">
                  <stringProp name="Authorization.url">${baseURL}</stringProp>
                  <stringProp name="Authorization.username">${user}</stringProp>
                  <stringProp name="Authorization.password">`1qwerty</stringProp>
                  <stringProp name="Authorization.domain">${domain}</stringProp>
                  <stringProp name="Authorization.realm"></stringProp>
                </elementProp>
              </collectionProp>
            </AuthManager>
            <hashTree/>
          </hashTree>
          <DurationAssertion guiclass="DurationAssertionGui" testclass="DurationAssertion" testname="Duration Assertion" enabled="true">
            <stringProp name="DurationAssertion.duration">${responseTimeout}</stringProp>
          </DurationAssertion>
          <hashTree/>
        </hashTree>
      </hashTree>
'''
res = ''


sample2 = '''
          <elementProp name="siteurlnum_%s" elementType="Argument">
            <stringProp name="Argument.name">siteurlnum_%s</stringProp>
            <stringProp name="Argument.value">http://atperf/sites/toplevelsite%s</stringProp>
            <stringProp name="Argument.metadata">=</stringProp>
          </elementProp>
'''

# for i in range(21,51):
	# res += sample % (i,i,i,i,i) + '\n'

for i in range(21,51):
	res += sample2 % (i,i,i-1) + '\n'
	
	
f = open('res1.txt', 'w')
f.write( res )
f.close()
	