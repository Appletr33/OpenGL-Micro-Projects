#version 300 es
out mediump vec4 FragColor;

in mediump vec3 ourColor;
in mediump vec2 TexCoord;

//texture sampler
uniform mediump sampler2D texture1;
uniform mediump sampler2D texture2;

void main()
{
    FragColor = mix(texture(texture1, TexCoord) * vec4(ourColor, 1.0), texture(texture2, TexCoord), 0.2);
}