import re
import sys

html_path = 'c:/Users/victus/.gemini/antigravity/scratch/cv_website/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Contact Info Hero replacement
c1 = '''          <div class="hero-contact">
            <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1rem;">
              <a href="tel:+4915757171746" class="contact-pill link-muted" style="padding: 0;">📞 +49 15757171746</a>
              <a href="mailto:Mohadeseh@mohadeseharianrad.de" class="contact-pill link-muted" style="padding: 0;">✉️ Mohadeseh@mohadeseharianrad.de</a>
              <a href="https://linkedin.com/in/mohadeseh-arianrad-30a826245" class="contact-pill link-muted" style="padding: 0;" target="_blank" rel="noopener noreferrer">🔗 linkedin.com/in/mohadeseh-arianrad-30a826245</a>
            </div>
            <a href="assets/Mohadeseh_Arianrad_CV.pdf" download class="contact-pill download-btn">Download CV</a>
          </div>'''
r1 = '''          <div class="hero-contact">
            <div class="contact-boxes">
              <a href="tel:+4915757171746" class="contact-box-link">📞 +49 15757171746</a>
              <a href="mailto:Mohadeseh@mohadeseharianrad.de" class="contact-box-link">✉️ Mohadeseh@mohadeseharianrad.de</a>
              <a href="https://linkedin.com/in/mohadeseh-arianrad-30a826245" class="contact-box-link" target="_blank" rel="noopener noreferrer">🔗 linkedin.com/in/mohadeseh-arianrad-30a826245</a>
            </div>
            <a href="assets/Mohadeseh_Arianrad_CV.pdf" class="contact-pill download-btn open-modal-link">Download CV</a>
          </div>'''
if c1 in html:
    html = html.replace(c1, r1)
else:
    print('Warning: Contact string not found')

# 2. Add Modal HTML and JS
html = html.replace('<script>', '''  <div id="iframeModal" class="modal">
    <div class="modal-content">
      <span class="close-modal">&times;</span>
      <iframe id="modalIframe" src="" frameborder="0"></iframe>
    </div>
  </div>

  <script>
    const modal = document.getElementById('iframeModal');
    const modalIframe = document.getElementById('modalIframe');
    const closeModal = document.querySelector('.close-modal');

    document.querySelectorAll('.open-modal-link').forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        modalIframe.src = this.href;
        modal.classList.add('show');
      });
    });

    closeModal.addEventListener('click', () => {
      modal.classList.remove('show');
      modalIframe.src = '';
    });

    window.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('show');
        modalIframe.src = '';
      }
    });
''')

# 3. Text Replacements for Accordions
t1 = '''            <br>
            <p>I have developed a particular specialization in Quantitative Methods in Finance. This area represents the
              intersection of my passion for statistical modeling and complex financial decision-making. My goal is to
              leverage my analytical rigor and engineering precision to provide high-level insights in quantitative
              analysis and financial management.</p>'''
rt1 = '''            <details class="resume-accordion">
              <summary>Read more</summary>
              <div class="accordion-content">
                <p>I have developed a particular specialization in Quantitative Methods in Finance. This area represents the
                  intersection of my passion for statistical modeling and complex financial decision-making. My goal is to
                  leverage my analytical rigor and engineering precision to provide high-level insights in quantitative
                  analysis and financial management.</p>
              </div>
            </details>'''
html = html.replace(t1, rt1)

t2 = '''            <p style="margin-top: 0.5rem;"><strong>Academic Leadership & Instruction</strong><br>
              Beyond my coursework, I was selected to mentor my peers and junior students in highly technical subjects:
            </p>
            <ul class="resume-list" style="margin-top: 0.5rem;">
              <li><strong>SolidWorks Instructor:</strong> I served as a primary instructor for junior students, teaching
                the complexities of 3D modeling, advanced assemblies, and technical drawings.</li>
              <li><strong>Teaching Assistant &ndash; Industrial Design:</strong> I provided technical problem-solving
                support and assisted junior students with their project development and course materials.</li>
            </ul>
            <p style="margin-top: 0.5rem;">For my thesis, I utilized Machine Learning and Data Mining methodologies to
              model and predict the Bullwhip (whiplash) effect across industrial supply chains, aiming to reduce
              inefficiencies through predictive analytics.</p>'''
rt2 = '''            <details class="resume-accordion">
              <summary>Read more</summary>
              <div class="accordion-content">
                <p style="margin-top: 0.5rem;"><strong>Academic Leadership & Instruction</strong><br>
                  Beyond my coursework, I was selected to mentor my peers and junior students in highly technical subjects:
                </p>
                <ul class="resume-list" style="margin-top: 0.5rem;">
                  <li><strong>SolidWorks Instructor:</strong> I served as a primary instructor for junior students, teaching
                    the complexities of 3D modeling, advanced assemblies, and technical drawings.</li>
                  <li><strong>Teaching Assistant &ndash; Industrial Design:</strong> I provided technical problem-solving
                    support and assisted junior students with their project development and course materials.</li>
                </ul>
                <p style="margin-top: 0.5rem;">For my thesis, I utilized Machine Learning and Data Mining methodologies to
                  model and predict the Bullwhip (whiplash) effect across industrial supply chains, aiming to reduce
                  inefficiencies through predictive analytics.</p>
              </div>
            </details>'''
html = html.replace(t2, rt2)

t3 = '''            <ul class="resume-list" style="margin-top: 0.5rem;">
              <li><strong>Maintaining Standards:</strong> I successfully supported the quality team through three IATF
                16949 certification audits during my time there. This involved coordinating with 5+ departments to
                ensure our daily work matched global automotive requirements.</li>
              <li><strong>Comprehensive Auditing:</strong> I conducted internal audits covering 20+ different processes
                and 80+ products to ensure technical compliance across the production line.</li>
              <li><strong>Documentation Support:</strong> I assisted in creating and updating 15+ procedures, forms,
                document and checklists to keep our documentation aligned with IATF standards. This effort helped reduce
                manual reporting errors by roughly 15%.</li>
            </ul>
            <p style="margin-top: 0.5rem;">Managing the high-integrity data required for three successful IATF audits is
              what initially drew me to quantitative analysis. I learned how to identify patterns and risks within
              complex industrial systems—a skill I am now advancing through Quantitative Methods in Finance in my
              Master's program.</p>'''
rt3 = '''            <details class="resume-accordion">
              <summary>Read more</summary>
              <div class="accordion-content">
                <ul class="resume-list" style="margin-top: 0.5rem;">
                  <li><strong>Maintaining Standards:</strong> I successfully supported the quality team through three IATF
                    16949 certification audits during my time there. This involved coordinating with 5+ departments to
                    ensure our daily work matched global automotive requirements.</li>
                  <li><strong>Comprehensive Auditing:</strong> I conducted internal audits covering 20+ different processes
                    and 80+ products to ensure technical compliance across the production line.</li>
                  <li><strong>Documentation Support:</strong> I assisted in creating and updating 15+ procedures, forms,
                    document and checklists to keep our documentation aligned with IATF standards. This effort helped reduce
                    manual reporting errors by roughly 15%.</li>
                </ul>
                <p style="margin-top: 0.5rem;">Managing the high-integrity data required for three successful IATF audits is
                  what initially drew me to quantitative analysis. I learned how to identify patterns and risks within
                  complex industrial systems—a skill I am now advancing through Quantitative Methods in Finance in my
                  Master's program.</p>
              </div>
            </details>'''
html = html.replace(t3, rt3)

t4 = '''            <p style="margin-top: 0.5rem;"><strong>The Problem: A Fragile Manual Workflow</strong><br>
              Before this automation, our quality tracking relied on a fragmented, manual chain that was extremely
              difficult to maintain accurately:</p>
            <ul class="resume-list" style="margin-top: 0.5rem;">
              <li><strong>High Complexity:</strong> Every product passed through several distinct processes, each
                requiring its own FMEA (Failure Mode and Effects Analysis) and tracking for multiple failure and rework
                types.</li>
              <li><strong>Manual Data Silos:</strong> Defect counts were manually recorded on the shop floor,
                transcribed into Excel, and then used to manually update RPN (Risk Priority Number) values in static
                Word documents.</li>
              <li><strong>High Risk of Error:</strong> With hundreds of data points moving between spreadsheets and text
                documents, the probability of transcription mistakes was high, which directly threatened the reliability
                of our risk assessments.</li>
            </ul>

            <p style="margin-top: 0.5rem;"><strong>The Technical Solution: The Pwark Engine</strong><br>
              I engineered Pwark to replace this manual chain with a single, validated digital workflow:</p>
            <ul class="resume-list" style="margin-top: 0.5rem;">
              <li><strong>Centralized Database:</strong> I moved all quality data into a Python-managed SQLite database,
                creating a single "source of truth" for the entire plant.</li>
              <li><strong>The "Word Doc" Challenge:</strong> I developed a custom extraction tool to pull data from
                unstructured Word-based FMEA files, transforming static documentation into dynamic, actionable data.
              </li>
              <li><strong>Automated Risk Calculation:</strong> The application automatically recalculates RPNs as
                failure data is entered, instantly flagging high-risk areas that require corrective action.</li>
            </ul>

            <p style="margin-top: 0.5rem;"><strong>The Practical Result</strong></p>
            <ul class="resume-list" style="margin-top: 0.5rem;">
              <li><strong>Reliability:</strong> By implementing automated validation schemas, I eliminated 99% of
                duplicate entries and significantly reduced the risk of human error in our reporting.</li>
              <li><strong>Efficiency:</strong> The system reduced data entry time by 40%, allowing the quality team to
                focus on resolving technical bottlenecks rather than managing paperwork.</li>
              <li><strong>Proactive Management:</strong> We moved from reactive reporting to real-time awareness,
                enabling us to generate monthly quality reports and corrective action documents instantly.</li>
            </ul>

            <p style="margin-top: 0.5rem;"><strong>The Quantitative Connection</strong><br>
              Building Pwark taught me that in complex systems, the highest risks often come from manual data handling.
              This experience in identifying and automating error-prone processes is what drives my current work in
              Quantitative Methods in Finance, where I apply the same principles of accuracy and validation to financial
              risk modeling.</p>'''
rt4 = '''            <details class="resume-accordion">
              <summary>Read more</summary>
              <div class="accordion-content">
                <p style="margin-top: 0.5rem;"><strong>The Problem: A Fragile Manual Workflow</strong><br>
                  Before this automation, our quality tracking relied on a fragmented, manual chain that was extremely
                  difficult to maintain accurately:</p>
                <ul class="resume-list" style="margin-top: 0.5rem;">
                  <li><strong>High Complexity:</strong> Every product passed through several distinct processes, each
                    requiring its own FMEA (Failure Mode and Effects Analysis) and tracking for multiple failure and rework
                    types.</li>
                  <li><strong>Manual Data Silos:</strong> Defect counts were manually recorded on the shop floor,
                    transcribed into Excel, and then used to manually update RPN (Risk Priority Number) values in static
                    Word documents.</li>
                  <li><strong>High Risk of Error:</strong> With hundreds of data points moving between spreadsheets and text
                    documents, the probability of transcription mistakes was high, which directly threatened the reliability
                    of our risk assessments.</li>
                </ul>

                <p style="margin-top: 0.5rem;"><strong>The Technical Solution: The Pwark Engine</strong><br>
                  I engineered Pwark to replace this manual chain with a single, validated digital workflow:</p>
                <ul class="resume-list" style="margin-top: 0.5rem;">
                  <li><strong>Centralized Database:</strong> I moved all quality data into a Python-managed SQLite database,
                    creating a single "source of truth" for the entire plant.</li>
                  <li><strong>The "Word Doc" Challenge:</strong> I developed a custom extraction tool to pull data from
                    unstructured Word-based FMEA files, transforming static documentation into dynamic, actionable data.
                  </li>
                  <li><strong>Automated Risk Calculation:</strong> The application automatically recalculates RPNs as
                    failure data is entered, instantly flagging high-risk areas that require corrective action.</li>
                </ul>

                <p style="margin-top: 0.5rem;"><strong>The Practical Result</strong></p>
                <ul class="resume-list" style="margin-top: 0.5rem;">
                  <li><strong>Reliability:</strong> By implementing automated validation schemas, I eliminated 99% of
                    duplicate entries and significantly reduced the risk of human error in our reporting.</li>
                  <li><strong>Efficiency:</strong> The system reduced data entry time by 40%, allowing the quality team to
                    focus on resolving technical bottlenecks rather than managing paperwork.</li>
                  <li><strong>Proactive Management:</strong> We moved from reactive reporting to real-time awareness,
                    enabling us to generate monthly quality reports and corrective action documents instantly.</li>
                </ul>

                <p style="margin-top: 0.5rem;"><strong>The Quantitative Connection</strong><br>
                  Building Pwark taught me that in complex systems, the highest risks often come from manual data handling.
                  This experience in identifying and automating error-prone processes is what drives my current work in
                  Quantitative Methods in Finance, where I apply the same principles of accuracy and validation to financial
                  risk modeling.</p>
              </div>
            </details>'''
html = html.replace(t4, rt4)


t5 = '''            <p style="margin-top: 0.5rem;"><strong>The Technical Approach</strong></p>
            <ul class="resume-list" style="margin-top: 0.5rem;">
              <li><strong>Data Preparation:</strong> I cleaned and processed multi-stage supply chain datasets to remove
                reporting inconsistencies and outliers before modeling.</li>
              <li><strong>Predictive Modeling:</strong> Using Scikit-learn, I developed a model to forecast demand and
                anticipate these "whiplash" effects.</li>
              <li><strong>Performance:</strong> The model achieved a low RMSE (Root Mean Square Error), ensuring the
                accuracy needed to optimize safety stock levels.</li>
            </ul>

            <p style="margin-top: 0.5rem;"><strong>The Impact</strong></p>
            <ul class="resume-list" style="margin-top: 0.5rem;">
              <li><strong>Inventory Efficiency:</strong> My findings suggested that using predictive models could reduce
                inventory distortion and safety stock requirements by 10–15%.</li>
              <li><strong>Optimization:</strong> This research demonstrated how data-driven demand forecasting can
                significantly lower holding costs and improve supply chain stability.</li>
            </ul>'''
rt5 = '''            <details class="resume-accordion">
              <summary>Read more</summary>
              <div class="accordion-content">
                <p style="margin-top: 0.5rem;"><strong>The Technical Approach</strong></p>
                <ul class="resume-list" style="margin-top: 0.5rem;">
                  <li><strong>Data Preparation:</strong> I cleaned and processed multi-stage supply chain datasets to remove
                    reporting inconsistencies and outliers before modeling.</li>
                  <li><strong>Predictive Modeling:</strong> Using Scikit-learn, I developed a model to forecast demand and
                    anticipate these "whiplash" effects.</li>
                  <li><strong>Performance:</strong> The model achieved a low RMSE (Root Mean Square Error), ensuring the
                    accuracy needed to optimize safety stock levels.</li>
                </ul>

                <p style="margin-top: 0.5rem;"><strong>The Impact</strong></p>
                <ul class="resume-list" style="margin-top: 0.5rem;">
                  <li><strong>Inventory Efficiency:</strong> My findings suggested that using predictive models could reduce
                    inventory distortion and safety stock requirements by 10–15%.</li>
                  <li><strong>Optimization:</strong> This research demonstrated how data-driven demand forecasting can
                    significantly lower holding costs and improve supply chain stability.</li>
                </ul>
              </div>
            </details>'''
html = html.replace(t5, rt5)

# Skills replacement
skills_old = '''        <ul class="resume-list">
          <li><strong>Programming:</strong> Python (Tkinter)</li>
          <li><strong>Databases:</strong> SQL, SQLite (Relational Schema Design, Foreign Keys)</li>
          <li><strong>Data Analysis:</strong> Pandas, Scikit-learn, Power BI</li>
          <li><strong>Version Control:</strong> Git</li>
          <li><strong>Quality Systems:</strong> IATF 16949 compliance processes</li>
        </ul>'''
skills_new = '''        <ul class="resume-list">
          <li><strong>Programming:</strong> Python</li>
          <li><strong>Databases:</strong> SQL</li>
          <li><strong>Data Analysis:</strong> Pandas, Scikit-learn, Power BI</li>
          <li><strong>Version Control:</strong> Git</li>
          <li><strong>Quality Systems:</strong> IATF 16949 compliance processes</li>
        </ul>'''
html = html.replace(skills_old, skills_new)

# Badges replacement
badges_old = '''          <a href="https://www.coursera.org/account/accomplishments/specialization/certificate/3XB9DYJW0JDJ"
            target="_blank" rel="noopener noreferrer" class="badge"
            style="text-decoration: none; color: inherit;">Generative AI for Data Analysts</a>
          <a href="https://www.coursera.org/account/accomplishments/records/ZVJCNGMKJRYP" target="_blank"
            rel="noopener noreferrer" class="badge" style="text-decoration: none; color: inherit;">Enhance your Data
            Analytics Career</a>
          <a href="https://www.coursera.org/account/accomplishments/records/1J1ADECMZGA5" target="_blank"
            rel="noopener noreferrer" class="badge" style="text-decoration: none; color: inherit;">Prompt Engineering
            Basics</a>
          <a href="https://www.coursera.org/account/accomplishments/records/24PV7Z4SRNZV" target="_blank"
            rel="noopener noreferrer" class="badge" style="text-decoration: none; color: inherit;">SQL for Data
            Science</a>
          <a href="https://drive.google.com/file/d/1ebnLLbH0U96LCokpka9U9m8IlMAb9W5m/view?usp=sharing" target="_blank"
            rel="noopener noreferrer" class="badge" style="text-decoration: none; color: inherit;">Data
            science</a>
          <a href="https://coursera.org/share/905f0844e455a6079871a469fd03a31f" target="_blank"
            rel="noopener noreferrer" class="badge" style="text-decoration: none; color: inherit;">Machine Learning for
            Supply Chain</a>'''

badges_new = '''          <a href="https://www.coursera.org/account/accomplishments/specialization/certificate/3XB9DYJW0JDJ"
            class="badge open-modal-link"
            style="text-decoration: none; color: inherit;">Generative AI for Data Analysts</a>
          <a href="https://www.coursera.org/account/accomplishments/records/ZVJCNGMKJRYP"
            class="badge open-modal-link" style="text-decoration: none; color: inherit;">Enhance your Data
            Analytics Career</a>
          <a href="https://www.coursera.org/account/accomplishments/records/1J1ADECMZGA5"
            class="badge open-modal-link" style="text-decoration: none; color: inherit;">Prompt Engineering
            Basics</a>
          <a href="https://www.coursera.org/account/accomplishments/records/24PV7Z4SRNZV"
            class="badge open-modal-link" style="text-decoration: none; color: inherit;">SQL for Data
            Science</a>
          <a href="https://drive.google.com/file/d/1ebnLLbH0U96LCokpka9U9m8IlMAb9W5m/preview"
            class="badge open-modal-link" style="text-decoration: none; color: inherit;">Data
            science</a>
          <a href="https://coursera.org/share/905f0844e455a6079871a469fd03a31f"
            class="badge open-modal-link" style="text-decoration: none; color: inherit;">Machine Learning for
            Supply Chain</a>'''
html = html.replace(badges_old, badges_new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html updated successfully!')
