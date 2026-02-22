# Smart Visual Assistant Setup Guide

## Overview
The Enhanced Smart Visual Assistant uses a multi-strategy approach to provide the best educational visual content:

1. **Primary Strategy**: AI-Generated Images (DALL-E)
2. **Secondary Strategy**: Educational Repositories (Wikimedia Commons)  
3. **Tertiary Strategy**: Refined Stock Photos (Pixabay)
4. **Fallback Strategy**: Educational Diagram Placeholders

## Required API Keys

### 1. OpenAI API Key (Primary Strategy - RECOMMENDED)

#### Getting Your API Key:
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to "API Keys" in your dashboard
4. Click "Create new secret key"
5. Copy the key (starts with `sk-...`)

#### Adding to Replit:
1. In your Replit project, click on "Secrets" (🔒) in the left sidebar
2. Click "New Secret"
3. Name: `OPENAI_API_KEY`
4. Value: Your OpenAI API key (sk-...)
5. Click "Add Secret"

#### Cost Considerations:
- DALL-E 3 costs ~$0.04 per 1024x1024 image
- For typical educational use (5-10 images per presentation), cost is $0.20-$0.40
- Images are generated once and can be reused
- High-quality, copyright-free educational diagrams

### 2. Pixabay API Key (Tertiary Strategy - OPTIONAL)

#### Getting Your API Key:
1. Go to [Pixabay API](https://pixabay.com/api/docs/)
2. Create a free Pixabay account
3. Your API key is shown in your account settings
4. Free tier: 20,000 requests per month

#### Adding to Replit:
1. Go to Secrets in Replit
2. Name: `PIXABAY_API_KEY`  
3. Value: Your Pixabay API key
4. Click "Add Secret"

### 3. Wikimedia Commons (No API Key Required)
- Wikimedia Commons is free and open
- No API key needed
- Provides educational diagrams and scientific illustrations
- All content is Creative Commons licensed

## Testing the Setup

### 1. Check API Key Configuration
Open the Replit console and look for these messages:
```
✅ OpenAI API key configured - DALL-E available
✅ Pixabay API key configured - stock photos available
ℹ️  Wikimedia Commons ready (no key required)
```

### 2. Test with Smart Visual Assistant
1. Go to Smart Visual Assistant in your app
2. Search for: "photosynthesis process"
3. Check the console logs for strategy used:
   - `🎨 [DALL-E] Successfully generated image` - Best outcome
   - `📚 [WIKIMEDIA] Found educational diagram` - Good outcome  
   - `🔍 [PIXABAY] Found relevant image` - Acceptable outcome
   - `📋 [PLACEHOLDER] Educational diagram` - Fallback

### 3. Test with Presentation Generator
1. Create a presentation on "Biology - Photosynthesis"
2. Generate slides and check which strategy provides images
3. Look for visual quality and educational relevance

## Strategy Priority Explanation

### Why DALL-E First?
- **Custom Educational Content**: Creates diagrams specifically for your topic
- **No Copyright Issues**: AI-generated content is copyright-free
- **Perfect Relevance**: Tailored exactly to your educational content
- **Professional Quality**: Clean, labeled scientific diagrams

### Why Wikimedia Second?
- **Educational Focus**: Specifically designed for educational use
- **High Quality**: Peer-reviewed scientific content
- **Free to Use**: All content is Creative Commons
- **Academic Standards**: Created by educational institutions

### Why Pixabay Third?
- **Large Selection**: Millions of images available
- **Commercial License**: Safe for educational and commercial use
- **Good Quality**: Professional photography and illustrations
- **Backup Option**: When specific educational content isn't available

### Placeholder as Fallback
- **Always Available**: Never fails to provide a result
- **Educational Focus**: Indicates where visual content should go
- **Professional Appearance**: Clean, branded educational placeholder

## Cost Management

### OpenAI DALL-E Costs:
- **Development/Testing**: ~$5-10/month for moderate use
- **Production Use**: ~$20-50/month for active educational platform
- **Cost Per Presentation**: ~$0.20-$0.40 (5-10 images)

### Free Alternatives:
- Wikimedia Commons: Completely free
- Pixabay: Free tier (20k requests/month)
- Educational placeholders: No cost

## Troubleshooting

### Common Issues:

1. **"DALL-E generation failed"**
   - Check OpenAI API key in Secrets
   - Verify account has credits/billing enabled
   - Check prompt isn't violating content policy

2. **"No educational content found"**
   - System will automatically fall back to next strategy
   - This is normal behavior for very specific topics

3. **"All strategies failed"**
   - Check internet connectivity
   - Verify API keys are correctly formatted
   - System will show educational placeholder

### Debug Mode:
Enable detailed logging by checking the Replit console during image generation. You'll see the complete strategy flow and any errors.

## Best Practices

1. **Use Descriptive Context**: "cellular respiration process" vs "biology"
2. **Add Keywords**: Include scientific terms for better AI generation
3. **Monitor Costs**: Check OpenAI usage dashboard regularly
4. **Quality Check**: Review generated images before using in presentations
5. **Fallback Ready**: Always have educational diagrams as backup content

## Integration Notes

The Enhanced Visual Assistant automatically integrates with:
- Presentation Generator (for slide images)
- Smart Visual Assistant page (for manual searches)
- Future educational tools (extensible architecture)

All strategies maintain consistent API responses, so switching between them is seamless for the end user.